# Final group Project
# CNA 330
# Teacher: Justin Elis
# NBA data will show important information such as the age weight and salary information accourding to the names of players and positions
#Group members: Francisco Espino, Ahmend

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

data = "https://raw.githubusercontent.com/Francisco-222/SQL-FINAL/main/nba%20players.csv" # This line will take the csv info from the github website, info which is according to the csv
 # I mean imports the data from nba players

# The code below will print the columns
data=pd.read_csv(data)
print(data.columns)   # prints all columns from nba players
data = data.dropna()   # remove unnecessary lines
data = data.where(pd.notnull(data), None)     # removes the lines which are empty


##### The code below will create connection with webmin

sql_engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/nba_finalsql') #sql_engine will help to connect with the nba_sql database
database_conn = sql_engine.connect()  # help to connect with the db
data.to_sql('nba players', con=database_conn, if_exists='replace', index=False)     # This will allow to export the csv data into the db webmin

#Code By Francisco E

#----------------------------------------------------------------------------------------------#
### To read pandas on console ###

# for weight, Number, Weight >>  data.tail()
# specify output of rows >> data[['Name', 'Team', 'Number']].head(3)
# for output the number of columns >> data.head(place the number here)
# output the players values >> data.values
# range index mean which is the last row stop      >>data.index
# output the number of colums and rows >> data.shape
# output the data types for each column >> data.dtypes
# output for the data colums >> data.columns
# output the index and colunm >> data.axes
# output the data csv information >> data.info()
#----------------------------------------------------------------------------------------------------#
## SOURCES ##
# Here I found the csv data and also some part of the pandas code:       https://www.geeksforgeeks.org/different-ways-to-import-csv-file-in-pandas/

# This source was especially helpful for the line number 29:              https://docs.sqlalchemy.org/en/13/core/engines.html

# It helped me to classify some doubts about db connection:               https://stackoverflow.com/questions/29355674/how-to-connect-mysql-database-using-pythonsqlalchemy-remotely

# Help for dataframe pandas:                                              https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html

# Video was helpful for plot                                               https://www.youtube.com/watch?v=a-im0rYzXJA&t=298s&ab_channel=JieJenn

# Documanation for plot too                                                https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.bar.html
