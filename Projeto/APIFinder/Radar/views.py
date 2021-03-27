from django.shortcuts import render
from .Finder import *
import json
import pymongo
from pymongo import MongoClient
import dns
from django.http import HttpResponse

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