
# Libraries
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#image1
#readcsv and grab columns
df=pd.read_csv('Scooby-Doo Complete - Episode List - Update 10 19 21.csv',usecols=['unmask.fred','unmask.daphne','unmask.velma','unmask.shaggy','unmask.scooby'])
#set height to count of boolean values occuring in each column
height =[df['unmask.fred'].sum(),df['unmask.daphne'].sum(),df['unmask.velma'].sum(),df['unmask.shaggy'].sum(),df['unmask.scooby'].sum()]
#set bar names
bars = ('Fred','Daphne','Velma','Shaggy','Scooby')
y_pos = np.arange(len(bars))
#label and appearance
plt.bar(y_pos, height,color='dodgerblue',edgecolor='black')
plt.xticks(y_pos, bars)
plt.xlabel('Character',fontsize=16)
plt.ylabel("Number of Unmaskings",fontsize=16)
plt.title("Which Scooby Doo Character Unmasked Most?",fontsize=16)
plt.show()


#image2
#read csv
df2=pd.read_csv('Scooby-Doo Complete - Episode List - Update 10 19 21.csv',usecols=['motive'])
height=df2['motive'].value_counts()
#use top 5
trimmed=height[0:5]
#make chart and labels
plt.bar(trimmed.index,trimmed.values,color='firebrick',edgecolor='black')
plt.xlabel('Motive',fontsize=16)
plt.ylabel("Number of Occurences",fontsize=16)
plt.title("Most Common Motive of Culprit",fontsize=16)
plt.show()

#image3
#readcsv and grab columns
df=pd.read_csv('Scooby-Doo Complete - Episode List - Update 10 19 21.csv',usecols=['snack.fred','snack.daphne','snack.velma','snack.shaggy','snack.scooby'])
#set height to count of boolean values occuring in each column
height =[df['snack.fred'].sum(),df['snack.daphne'].sum(),df['snack.velma'].sum(),df['snack.shaggy'].sum(),df['snack.scooby'].sum()]

#set bar names
bars = ('Fred','Daphne','Velma','Shaggy','Scooby')
y_pos = np.arange(len(bars))
#label and appearance
plt.bar(y_pos, height,color='burlywood',edgecolor='black')
plt.xticks(y_pos, bars)
plt.xlabel('Character',fontsize=16)
plt.ylabel("Number of Scooby Snacks Given",fontsize=16)
plt.title("Which Scooby Doo Character Gave the Most Scooby Snacks?",fontsize=14)
plt.show()

