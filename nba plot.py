import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

##### PLot #### will show the avarages of age and weight of NBA players

data = "https://raw.githubusercontent.com/Francisco-222/SQL-FINAL/main/nba%20players.csv" # This line will take the csv info from the github website, info which is according to the csv
 # I mean imports the data from nba players


sql_engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/nba_finalsql') #sql_engine will help to connect with the nba_sql database

# The code below will print the columns
data=pd.read_sql_table('nba players',sql_engine)

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
insert_data_labels(barPG) ###PG mean the position of point guard in the ground
insert_data_labels(barSF) ## this is Small forward in feild
plt.show()
