from django.shortcuts import render
from .Finder import *
import json
import pymongo
from pymongo import MongoClient
import dns
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
        
        
# Create your views here.
@csrf_exempt
def BuscarCurriculo(request, pk):
   myclient = pymongo.MongoClient("mongodb+srv://dbUser:system@cluster0.5hlez.mongodb.net/Finder?retryWrites=true&w=majority")
   mydb = myclient["Finder"]
   mycol = mydb["curriculo"]

   myquery = { "_id": pk }

   mydoc = mycol.find(myquery)

   for x in mydoc:
      print(x)

   return HttpResponse("Curriculo encontrado com sucesso!")
 

@csrf_exempt
def CadastrarCurriculo(request):

   if request.method == "POST":
         myclient = pymongo.MongoClient("mongodb+srv://dbUser:system@cluster0.5hlez.mongodb.net/Finder?retryWrites=true&w=majority")
         mydb = myclient["Finder"]
         mycol = mydb["curriculo"]

         newcurriculo = json.loads(request.body)
         mydoc = mycol.insert_one(newcurriculo)

   return HttpResponse("Curriculo cadastrado com sucesso!")

