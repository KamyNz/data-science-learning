import sys,os
import csv
import pandas as pd
def getting_path():
    base_folder = os.path.dirname(__file__)
    # getting file name after path
    file_name = os.path.join(os.getcwd(),base_folder,"data","icfes_renata_taller.csv")
    #print(file_name)


def processing_csv():
    #with open(getting_path()) as csv_file:
    #csv_reader = c.reader(csv_file, delimiter=';')
    pdf = pd.read_csv("/home/estuvar4/Desktop/camila_folder/caoba_prueba/data/icfes_renata_taller.csv",sep=";")
    pdfcolejornada = pdf.groupby('COLE_JORNADA')['PUNT_GLOBAL'].mean()
    print(pdfcolejornada.to_json())

getting_path()
processing_csv()
    

	
