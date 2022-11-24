
from datetime import datetime
start_time = datetime.now()
import openpyxl
import pandas as pd
import os
from datetime import datetime
start_time = datetime.now()
 #opening pakistan inning file
Pakistan_Inning = open("Pak_Innings1.txt","r+") 
 #opening india inning file
India_Inning = open("india_inns2.txt","r+")
#reading teams text file
teams = open("teams.txt","r+")
team = teams.readlines()
 
Pakistan_team = team[0]
#spliting at ','
pakistan_players = Pakistan_team[23:-1:].split(",")
#spliting at ','
India_team = team[2]
India_players = India_team[20:-1:].split(",")


India  = India_Inning.readlines() 
for i in India:         #removing line space
    if i=='\n':
        India.remove(i)
      

Pakistan = Pakistan_Inning.readlines() 
for i in Pakistan:
    if i=='\n':                   #removing line space
        Pakistan.remove(i)

wb = openpyxl.Workbook()
ws = wb.active                


India_Fall_of_wickets=0
Pakistan_fall_of_wickets=0
Pakistan_Byes=0                 #created new variables for counting
Pakistan_bowlers_total=0


Out_Pakistan_batsman={}
India_bowlers={}
India_bats={}              #created empty dictionary
Pakistan_bats={}
Pakistan_bowlers={}




