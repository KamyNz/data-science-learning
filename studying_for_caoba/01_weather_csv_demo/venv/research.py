import os
import csv
import collections  # Using namedtuple to structure data using a Record
from typing import List # Using typing to get list of record and easily use string formating over them

data = [] # LIST OF RECORDS OF THA SEATTLE WEATHER DATA

Record = collections.namedtuple(
    'Record',
    'date,actual_mean_temp,actual_min_temp,actual_max_temp,'
    'average_min_temp,average_max_temp,record_min_temp,record_max_temp,'
    'record_min_temp_year,record_max_temp_year,'
    'actual_precipitation,average_precipitation,record_precipitation'
)


def init():
    # using from os module to get path of file
    #base_folder = os.path.dirname(__file__)
    #print(base_folder)

    base_folder = "/home/asisbio2/Documents/data-science-learning/studying_for_caoba/weather_csv_demo/"

    # getting file name after path
    file_name = os.path.join(base_folder,"data","seattle.csv")

    # Before
    #with open(file_name,'r',encoding='utf-8') as fin:
    #    print(fin.read())

    # using functions from module csv
    with open(file_name,'r',encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        data.clear()

        for row in reader:

            # Before
            # print("ROW --> {}".format(row))
            #print(row.get('actual_mean_temp'),
            #      row.get('actual_precipation'))

            record = parse_row(row)
            data.append(record)
            #print(type(record.actual_max_temp),record.date)

def parse_row(row):
    #date,
    # actual_mean_temp,
    # actual_min_temp,
    # actual_max_temp,
    # average_min_temp, average_max_temp,
    # record_min_temp, record_max_temp, record_min_temp_year, record_max_temp_year,
    # actual_precipitation, average_precipitation, record_precipitation

    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])

    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])

    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])

    record = Record(
        #date = row.get(date) # There is a short hand to do this
        **row
    )
    return(record)

def hot_days() -> List[Record]:

    # since data is a list WHE CAN USED A LAMBDA FUNCTION TO GET THE RECORDS SORTED FROM HIGHEST TO LOWEST
    sorted_hot_days = sorted(data,key=lambda r: r.actual_max_temp,reverse=True)
    return(sorted_hot_days)

def cold_days() -> List[Record]:

    # since data is a list WHE CAN USED A LAMBDA FUNCTION TO GET THE RECORDS SORTED FROM HIGHEST TO LOWEST
    sorted_cold_days = sorted(data,key=lambda r: r.actual_max_temp)
    return(sorted_cold_days)

def wet_days() -> List[Record]:
    # we can us -r.actual_precipation if we do not want to use reverse=True
    sorted_wet_days = sorted(data,key=lambda r: -r.actual_precipitation)
    return(sorted_wet_days)
