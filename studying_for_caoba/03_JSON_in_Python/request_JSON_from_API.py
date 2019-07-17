#!python3
import os,sys
# importing json from API
import json
import requests
from pprint import pprint

def init():
    # using from os module to get path of file
    base_folder = os.path.dirname(__file__)
    #print(base_folder)

    #base_folder = "/home/asisbio2/Documents/data-science-learning/studying_for_caoba/03_JSON_in_Python/"
    #print(os.getcwd())
    #print(base_folder)

    # getting file name after path
    file_name = os.path.join(os.getcwd(),base_folder,"data","mount-data.json")
    #print(file_name)

    with open(file_name,'r') as fjsonin:
        data = json.load(fjsonin)

    return(data)

def init2():
    #r = requests.get('https://us.api.battle.net/wow/character/Cenarion%20Circle/Ardy?fields=mounts&locale=en_US&apikey=')
    #pprint()
    
    #First print
    data = json.loads(r.text)
    for item in data.items():
        pprint(item)

def init3(data):
    #First print
    #data = json.loads(r.text)
    for item in data.items():
        pprint(item)

#data = init()
#init3(data)
#init2()
#init3()
