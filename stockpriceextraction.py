#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:55:11 2020

@author: kianweelee
"""


# Importing packages
import pymysql
import config.setting
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# Create a user input to ask users to type in the stock symbol (eg: AMD, EDIT, NVO)
stock_input = str(input("Please kindly input your code symbol\n"))

# Using the yfinance to generate the dataframe containing the stock
df = yf.download(tickers = stock_input,
	period= "1d",
	interval="1m")

# Add in new column with the stock name
df['Symbol']=stock_input

# Rename Adj close column name to ommit whitespace
df.rename(columns={'Adj Close':'Adj_Close'}, inplace=True)

# Round all values to 2 decimal places
df = df.round(2)

#____________________________SQL_____________________________________________________
#Save event data to database
# Open database connection

table_bool = str(input("Do you have an existing table to store your data? Y/N\n"))

while table_bool.lower() not in ('y','n'):
	table_bool = str(input("Do you have an existing table to store your data? Y/N\n"))

# If user has a table, ask for table name:
if table_bool == 'y':
	table_name = str(input("Please tell us your table name:\n"))
	engine = create_engine('mysql+pymysql://{user}:{password}@localhost/{database_name}'.format(user = config.setting.db_user, password = config.setting.db_password, database_name = config.setting.db_name))
	df.to_sql(name='{name}'.format(name = table_name), con=engine, if_exists = 'append', index=False)
	print("Data successfully exported!")

else:
	new_table = str(input("What will you like to name your table?\n"))
	conn = pymysql.connect(host=config.setting.host, user=config.setting.db_user, passwd=config.setting.db_password, db = config.setting.db_name)
	conn.cursor().execute("CREATE TABLE IF NOT EXISTS {new_name} (Open DECIMAL(4,2), High DECIMAL(4,2), Low DECIMAL(4,2), Close DECIMAL(4,2), Adj_Close DECIMAL(4,2), Volume INT, Symbol VARCHAR(5) ) ".format(new_name = new_table))
	engine = create_engine('mysql+pymysql://{user}:{password}@localhost/{database_name}'.format(user = config.setting.db_user, password = config.setting.db_password, database_name = config.setting.db_name))
	df.to_sql(name='{new_name}'.format(new_name = new_table), con=engine, if_exists = 'append', index=False)
	print("Data successfully exported!")
