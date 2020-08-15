#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:55:11 2020

@author: kianweelee
"""


# Importing packages
import mysql.connector
import urllib.request
import json 
from dateutil import parser
import config.setting

# Create a user input to ask users to type in the stock symbol (eg: AMD, EDIT, NVO)
stock_input = str(input("Please kindly input your code symbol\n"))

# Using package urllib to read url
url = ("https://api.nasdaq.com/api/quote/{}/chart?assetclass=stocks".format(stock_input))

# Create fake browser visit
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)	

htmltext = urllib.request.urlopen(req)

# Parse json string and return a dict
data = json.load(htmltext)


def preprocessing(data):
    '''
    
    Parameters
    ----------
    data : Dict
        Contains a chart list that has datetime and prices 

    Returns
    -------
    A parameter containing tuples in this format:
        (datetime (DATETIME), prices (FLOAT), symbol (STR))
        
    '''

    # Looking into the dictionary and extracting out key = 'chart' data
    data1 = (data['data']['chart'])
    
    # Creating a list of time and prices 
    date = data['data']['timeAsOf'] # Contains date in mm dd, yyyy format
    time = []
    prices = []
    for i in data1:
        time.append((i['z']['dateTime'])+ " " + date) # combine date and time together
        prices.append((i['y']))
    
    # time is in string format. Need to convert to datetime format to add into SQL
    new_time = ([parser.parse(x) for x in time])  
    
    # Creating a list of tuples containing the parameters (datetime, prices, symbol)
    param_lst = []
    for i in range(0, len(prices)):
        k = ((new_time[i], prices[i], stock_input))
        param_lst.append(k)
    return param_lst

#____________________________SQL_____________________________________________________
#Save event data to database
# Open database connection
db = mysql.connector.connect(user= config.setting.db_user , password= config.setting.db_password,
                             host='127.0.0.1',database='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()
   

# Prepare SQL query to INSERT a record into the database.

sql = "INSERT INTO nasdaq(datetime, prices, symbol) VALUES (%s, %s, %s)"
try:
    # Execute the SQL command with the required parameters
    cursor.executemany(sql, preprocessing(data))
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
    # disconnect from server
    db.close()
