import requests
import json
import urllib
from sqlalchemy import create_engine

def add_fun(num1, num2):
    return (num1 + num2)


def createDatabase():
    #create database cars; 
    return 

def getData():
    where = urllib.parse.quote_plus("""
    {
        "Year": {
        "$exists": true
        }
    }
    """)

    url = 'https://parseapi.back4app.com/classes/Carmodels_Car_Model_List_Ferrari?count=1&limit=0&where=%s' % where
    headers = {
    'X-Parse-Application-Id': 'RcA7xAHt05iSSYfQAq5O6IP9s16Askxnc07XJ7t1', # This is your app's application id
    'X-Parse-REST-API-Key': '1rUQAkAwRg5133HdwtCPbw0IiaHcpVji74Z38ZQf' # This is your app's REST API key
    }
    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
    print(json.dumps(data, indent=2))

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
