#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:13:42 2020

@author: kianweelee
"""

# Importing packages
import mysql.connector
import urllib
import re
import json 
from dateutil import parser
import datetime

# Create a user input to ask users to type in the stock symbol (eg: AMD, EDIT, NVO)
stock_input = str(input("Please kindly input your code symbol\n"))

# Using package urllib to read url
htmltext = urllib.request.urlopen("https://api.nasdaq.com/api/quote/{}/chart?assetclass=stocks".format(stock_input))

# Parse json string and return a dict
data = json.load(htmltext)

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

#____________________________SQL_____________________________________________________

#Save event data to database
# Open database connection
db = mysql.connector.connect(user='root', password='password',
                             host='127.0.0.1',database='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()
   

# Prepare SQL query to INSERT a record into the database.

for index in range(0, len(prices)):
    sql = "INSERT INTO {}(datetime, prices) VALUES ('{}', '{}')".format(stock_input,new_time[index], prices[index])
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        # disconnect from server
        db.close()


































