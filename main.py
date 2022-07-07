import requests
import json
import urllib
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)

def add_fun(num1, num2):
    return (num1 + num2)


def createDatabase():
    #create database cars; 
    return 

def getData():
    url = 'https://vpic.nhtsa.dot.gov/api//vehicles/GetMakesForManufacturerAndYear/mer?year=2013&format=json';
    r = requests.get(url);
    print(type(r.text));

    df = pd.read_json(r.text)
    print("from json to df ", df.head())
    #need to get json Results column to a df
    #https://www.geeksforgeeks.org/python-pandas-flatten-nested-json/
    normaldf = pd.json_normalize(df["Results"])
    print("results normalized ", normaldf.head())

    #df to sql
    normaldf.to_sql('newDB', con=engine)
    print("new database type ", type('newDB'))

    #query result goes to a dataframe
    alphabetized = engine.execute("SELECT MakeName FROM newDB ORDER BY MakeName ASC limit 10;")  
    print("alpha names from query ", pd.DataFrame(alphabetized))


def createTable():
    '''CREATE TABLE mytable ( 
	    id INT(8) UNSIGNED NOT NULL auto_increment,
	    model VARCHAR(255) default NULL,
	    year YEAR(4) default NULL,
	    brand VARCHAR(255) default NULL,
	    PRIMARY KEY (id)
	) AUTO_INCREMENT=1;'''

print('main.py here')
getData()
