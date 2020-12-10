# Final group Project
# CNA 330
# Teacher: Justin Elis
# NBA data will show important information such as the age weight and salary information accourding to the names of players and positions
#Group members: Francisco Espino, TJ, Ahmend

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

##### PLot #### will show the avarages of age and weight of NBA players

subjects = ['Age', 'Weight', ] #    Will going to show the average between age and weight; However we can use any subjects from csv just we need to change info inside of []
dataset = data.groupby('Position')[subjects].mean() # Will are combinate the subject with position
indx = np.arange(len(subjects))
score_label = np.arange(50, 300, 50) # number represent label size
PG_means = list(dataset.T['PG']) # In this case we pick only two position which is PG and SF, remember we can use any position for the plot
SF_means = list(dataset.T['SF']) # second position that I pick for the plot
bar_width = 0.35 # represent the width size
fig, ax = plt.subplots()  # use the variable ax to create the subplots
barPG = ax.bar(indx - bar_width/2, PG_means, bar_width, label='PG_means')  # will print the subplot means
barSF = ax.bar(indx + bar_width/2, SF_means , bar_width, label='SF_means') # will print the subplot means
# Both below inserting x axis label
ax.set_xticks(indx)
ax.set_xticklabels(subjects)
# Both below inserting y axis label
ax.set_yticks(score_label)
ax.set_yticklabels(score_label)
# All code below inserting legend, mean insert the ax and y values
ax.legend()
def insert_data_labels(bars):
   for bar in bars:
      bar_height = bar.get_height()
      ax.annotate('{0:.0f}'.format(bar.get_height()),
         xy=(bar.get_x() + bar.get_width() / 2, bar_height),
         xytext=(0, 3),
         textcoords='offset points',
         ha='center',
         va='bottom'
      )


# Code of below will print the bar data from csv
insert_data_labels(barPG) ###PG mean the position of point guard
insert_data_labels(barSF) ## this is Small forward
plt.show()

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