from django.shortcuts import render
from .Finder import *
import json
import pymongo
from pymongo import MongoClient
import dns
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#finder_instance = None

#def init(self):
 #       self.finder_instance = Finder()
        
        
# Create your views here.
def home(self):
   myclient = pymongo.MongoClient("mongodb+srv://dbUser:system@cluster0.5hlez.mongodb.net/Finder?retryWrites=true&w=majority")
   mydb = myclient["Finder"]
   mycol = mydb["curriculo"]

   myquery = { "nome": "arthur cardoso" }

   mydoc = mycol.find(myquery)

   for x in mydoc:
      print(x)

   return HttpResponse("Welcome to poll's index!")
   # finder_instance = Finder()
   
   # myquery = { "nome": "arthur cardoso" }
   # result = finder_instance.search(myquery)

   # if result.count() == 0:
   #    print("Nenhum curriculo encontrado...")

   # else:
   #    for jsn in result:
   #       print(jsn['_id'])

@csrf_exempt
def buscarvaga(request):
   vaga = request.POST.get('id_vaga')
   #  vaga = vaga.objects.get(_id=id_vaga)

   if request.method == "POST":
         myclient = pymongo.MongoClient("mongodb+srv://dbUser:system@cluster0.5hlez.mongodb.net/Finder?retryWrites=true&w=majority")
         mydb = myclient["Finder"]
         mycol = mydb["vaga"]

         myquery = { "urgencia": "baixa" }

         mydoc = mycol.find(myquery)
      #   return redirect('/tarefas')
         for x in mydoc:
            print(x)
   return HttpResponse("Achou!")
 
#  context = {'task': task}
#  return render(request, 'bridges_app/delete_tarefa.html', context)