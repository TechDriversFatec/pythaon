import json
import pymongo
import dns
from pycep_correios import get_address_from_cep, WebService
from geopy.geocoders import Nominatim
from math import sin, cos, sqrt, atan2, radians
from geopy import distance
from haversine import haversine, Unit
from .Finder import *

from pymongo import MongoClient

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from bson import ObjectId
from bson.json_util import dumps
from bson.objectid import ObjectId
        
def createConnection():
   return pymongo.MongoClient("mongodb+srv://dbUser:system@cluster0.5hlez.mongodb.net/Finder?retryWrites=true&w=majority")

def getAdressByCep(cep):
   endereco = get_address_from_cep(cep, webservice=WebService.CORREIOS)
   print(endereco['logradouro'] + ", " + endereco['cidade'])
   geolocator = Nominatim(user_agent="APIFinder")
   return geolocator.geocode(endereco['logradouro'] + ", " + endereco['cidade'] + " - " + endereco['bairro'])

@csrf_exempt
def buscarvaga(request, pk):
   if request.method == "GET":
      client = createConnection()
      db = client["Finder"]
      col = db["vagas"]
  
      vaga = col.find_one({"VagaIdExterno" : pk})
      
      if vaga:
         return JsonResponse(dumps(vaga), safe=False)
      else:
         return JsonResponse({"message" : "Vaga não encontrada."}, status=200)
   else:
      return JsonResponse({"message": "Erro na requisição. Método esperado: GET."}, status=500)
  
@csrf_exempt
def insert_vaga(request):
   if request.method == "POST":
      client = createConnection()
      db = client["Finder"]
      col = db["vagas"]
      
      result = col.insert_one(json.loads(request.body))
      # result
      return JsonResponse({"message" : "Vaga cadastrada com sucesso."}, status=200)
   else:
      return JsonResponse({"message": "Erro na requisição. Método esperado: POST."}, status=500)

@csrf_exempt
def updatevaga(request, pk):
   if request.method == "PUT":
      client = createConnection()
      db = client["Finder"]
      col = db["vagas"]
      col.g
      result = col.update_one({"VagaIdExterno" : pk}, json.loads(request.body))
      # result
      return JsonResponse({"message":"Vaga atualizada com sucesso."}, status=200)
   else:
      return JsonResponse({"message":"Erro na requisição. Método esperado: PUT."}, status=500)  

@csrf_exempt
def delete_vaga(request, pk):
   if request.method == "DELETE":
      client = createConnection()
      db = client["Finder"]
      col = db["vagas"]

      db.collection.create_index({ "vaga" : "2dsphere" })
      
      result = col.delete_many({"VagaIdExterno": pk})
      # result
      return JsonResponse({"message":"Vaga excluida com sucesso."}, status=200)
   else:
      return JsonResponse({"message":"Erro na requisição. Método esperado: DELETE."}, status=500) 

@csrf_exempt
def buscarCurriculo(request, pk):
   if request.method == 'GET':
      client = createConnection()
      db = client["Finder"]
      curriculos = db["Inscrito"]

      curriculo = curriculos.find_one({ "InscritoIdExterno": pk })

      if curriculo:
         return JsonResponse(dumps(curriculo), safe=False)
      else:
         return JsonResponse({"message" : "Curriculo não encontrado."}, status=200)
   else:
      return JsonResponse({"message": "Erro na requisição. Método esperado: GET."}, status=500)

@csrf_exempt
def cadastrarCurriculo(request):
   if request.method == "POST":
      client = createConnection()         
      db = client["Finder"]
      col = db["Inscrito"]

      result = col.insert_one(json.loads(request.body))
      # result
      return JsonResponse({"message":"Curriculo inserido com sucesso."}, status=200)
   else:
      return JsonResponse({"message":"Erro na requisição. Método esperado: POST."}, status=500) 

@csrf_exempt
def atualizarCurriculo(request, pk):
   if request.method == "PUT":
      client = createConnection()
      db = client["Finder"]
      col = db["Inscrito"]

      result = col.update_one({"InscritoIdExterno" : pk}, json.loads(request.body))
      # result
      return JsonResponse({"message":"Curriculo atualizado com sucesso."}, status=200)
   else:
      return JsonResponse({"message":"Erro na requisição. Método esperado: PUT."}, status=500)   

@csrf_exempt
def deletarCurriculo(request, pk):
   if request.method == "DELETE":
      client = createConnection()
      db = client["Finder"]
      col = db["Inscrito"]

      result = col.delete_many({"InscritoIdExterno" : pk})
   # result
      return JsonResponse({"message" : "Curriculo excluido com sucesso."}, status=200)
   else:
      return JsonResponse({"message" : "Erro na requisição. Método esperado: DELETE."}, status=500)   

@csrf_exempt
def buscarPorVagaVT0(request,VagaID):
   if request.method == 'GET':
      client = createConnection()
      db = client["Finder"]
      vaga = db["vagas"]
      curriculos = db["Inscrito"]
      vaga = vaga.find_one({"VagaIdExterno" : VagaID})  
      query = { 
         "$or" : [
         {"coordenadas": {"$near": {"$maxDistance": 3000, "$geometry":{"type": "Point", "coordinates":[vaga['coordenadas']['coordinates'][0], vaga['coordenadas']['coordinates'][1]]}}}}
         ]
       }
      result_curriculos = curriculos.find(query)
      if result_curriculos:
         IdCol = [str(result['_id']) for result in result_curriculos]
         IdExterno = [str(result['InscritoIdExterno']) for result in result_curriculos]
         return JsonResponse({
                  "candidatos" : IdCol,
                  "IdExterno" : IdExterno,
                  "message" : ""
                  })
      else:
         return JsonResponse({
                  "candidatos" : [],
                  "message" : "Nenhum candidato encontrado para esta vaga."
                  }, status=200)

      return JsonResponse({"message" : "Vaga não encontrada."}, status=200)
   else:
      return JsonResponse({"message" : "Vaga não encontrada."}, status=200)

@csrf_exempt
def buscarPorVaga(request,VagaID):
   if request.method == 'GET':
      # Inicia conexão com o banco
      client = createConnection()

      mydb = client["Finder"]
      curriculos = mydb["Inscrito"]
      vagas = mydb["vagas"]

      # Recupera a vaga recebida por parâmetro
      vaga = vagas.find_one({"_id" : ObjectId(VagaID)})

      if vaga:
         searchRequisitos = '|'.join([str(requisito['descricao']) for requisito in vaga['competencia']])

         query = {
            "$or" : [ 
               # { "tipoContratoDesejadoInscrito" : { "$regex": vaga['tipoContratacaoPerfilVaga'] } },
               { "perfilProfissionalTituloInscrito" : { "$regex":searchRequisitos } },
               { "perfilProfissionalDescricaoInscrito" : { "$regex": searchRequisitos } },
               { "experienciaProfissional.descricao": { "$regex": searchRequisitos } },
               { "formacao.curso": { "$regex": searchRequisitos } },
               { "competencia.descricao": { "$regex": searchRequisitos } } 
            ] 
         }

         result_curriculos = curriculos.find(query)

         if result_curriculos:
            IdCol = [str(result['_id']) for result in result_curriculos]
            return JsonResponse({
                                 "candidatos" : IdCol,
                                 "message" : ""
                              })
         else:
            return JsonResponse({
                                 "candidatos" : [],
                                 "message" : "Nenhum candidato encontrado para esta vaga."
                              }, status=200)
      else:
         return JsonResponse({"message" : "Vaga não encontrada"}, status=200)
   else:
      return JsonResponse({"message": "Erro na requisição. Método esperado: GET."}, status=500)
