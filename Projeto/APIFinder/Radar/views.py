from django.shortcuts import render
from Finder import init, search
import json
import requests
import urllib.request
import pymongo
from pymongo import MongoClient

# Create your views here.
def home():
        finder_instance = Finder()

        myquery = { "nome": "arthur cardoso" }
        result = finder_instance.search(myquery)

        if result.count() == 0:
           print("Nenhum curriculo encontrado...")

        else:
            for jsn in result:
             print(jsn['_id'])