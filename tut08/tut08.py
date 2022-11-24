
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




for l in Pakistan:
    x=l.index(".")
    Pak_over =l[0:x+2]
    temp=l[x+2::].split(",")
    Current_Ball=temp[0].split("to") #0 2

    if f"{Current_Ball[0].strip()}" not in India_bowlers.keys() :
        India_bowlers[f"{Current_Ball[0].strip()}"]=[1,0,0,0,0,0,0]   
    elif "wide" in temp[1]:
        pass
    elif "bye" in temp[1]:
        if "FOUR" in temp[2]:
            Pakistan_Byes+=4
        elif "1" in temp[2]:
            Pakistan_Byes+=1            #over0,
        elif "2" in temp[2]:            #NB4
            Pakistan_Byes+=2            #medan1
        elif "3" in temp[2]:            #runs2
            Pakistan_Byes+=3            #Wickets3,
        elif "4" in temp[2]:            #ECO6
            Pakistan_Byes+=4            # WD5, 
        elif "5" in temp[2]:
            Pakistan_Byes+=5

    else:
        India_bowlers[f"{Current_Ball[0].strip()}"][0]+=1
    
    if f"{Current_Ball[1].strip()}" not in Pakistan_bats.keys() and temp[1]!="wide":
        Pakistan_bats[f"{Current_Ball[1].strip()}"]=[0,1,0,0,0]                #runs ,ball ,4s ,6s , sr
    elif "wide" in temp[1] :
        pass
    else:
        Pakistan_bats[f"{Current_Ball[1].strip()}"][1]+=1
    

    if "out" in temp[1]:
        India_bowlers[f"{Current_Ball[0].strip()}"][3]+=1
        if "Bowled" in temp[1].split("!!")[0]:
            Out_Pakistan_batsman[f"{Current_Ball[1].strip()}"]=("b" + Current_Ball[0])
        elif "Caught" in temp[1].split("!!")[0]:
            w=(temp[1].split("!!")[0]).split("by")                                                        #this is for wicket criteria 
            Out_Pakistan_batsman[f"{Current_Ball[1].strip()}"]=("c" + w[1] +" b " + Current_Ball[0])
        elif "Lbw" in temp[1].split("!!")[0]:
            Out_Pakistan_batsman[f"{Current_Ball[1].strip()}"]=("lbw  b "+Current_Ball[0])

    

    if "no run" in temp[1] or "out" in temp[1] :
        India_bowlers[f"{Current_Ball[0].strip()}"][2]+=0
        Pakistan_bats[f"{Current_Ball[1].strip()}"][0]+=0
    elif "1 run" in temp[1]:
        India_bowlers[f"{Current_Ball[0].strip()}"][2]+=1
        Pakistan_bats[f"{Current_Ball[1].strip()}"][0]+=1
    elif "2 run" in temp[1]:
        India_bowlers[f"{Current_Ball[0].strip()}"][2]+=2
        Pakistan_bats[f"{Current_Ball[1].strip()}"][0]+=2
    elif "3 run" in temp[1]:
        India_bowlers[f"{Current_Ball[0].strip()}"][2]+=3          #this is for pakistan battin)and inia bowling counting
        Pakistan_bats[f"{Current_Ball[1].strip()}"][0]+=3
    elif "4 run" in temp[1]:
        India_bowlers[f"{Current_Ball[0].strip()}"][2]+=4
        Pakistan_bats[f"{Current_Ball[1].strip()}"][0]+=4
    elif "FOUR" in temp[1]:
        India_bowlers[f"{Current_Ball[0].strip()}"][2]+=4
        Pakistan_bats[f"{Current_Ball[1].strip()}"][0]+=4
        Pakistan_bats[f"{Current_Ball[1].strip()}"][2]+=1
    elif "SIX" in temp[1]:
        India_bowlers[f"{Current_Ball[0].strip()}"][2]+=6
        Pakistan_bats[f"{Current_Ball[1].strip()}"][0]+=6
        Pakistan_bats[f"{Current_Ball[1].strip()}"][3]+=1
    elif "wide" in temp[1]:
        if "wides" in temp[1]:
            India_bowlers[f"{Current_Ball[0].strip()}"][2]+=int(temp[1][1])
            India_bowlers[f"{Current_Ball[0].strip()}"][5]+=int(temp[1][1])
        else:
            India_bowlers[f"{Current_Ball[0].strip()}"][2]+=1
            India_bowlers[f"{Current_Ball[0].strip()}"][5]+=1

for val in Pakistan_bats.values():
    val[-1]=round((val[0]/val[1])*100 , 2)




####this is same for india inning as for pakistan batting
India_bowlers_total=0
ind_byes=0
out_ind_bat={}
for l in India:
    x=l.index(".")
    over_ind=l[0:x+2]

    temp=l[x+2::].split(",")

    Current_Ball=temp[0].split("to") #0 2
    if f"{Current_Ball[0].strip()}" not in Pakistan_bowlers.keys() :
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"]=[1,0,0,0,0,0,0]   #over0, medan1, runs2, Wickets3, NB4, WD5, ECO6
    elif "wide" in temp[1]:
        pass
    elif "bye" in temp[1]:
        if "FOUR" in temp[2]:
            ind_byes+=4
        elif "1" in temp[2]:
            ind_byes+=1
        elif "2" in temp[2]:
            ind_byes+=2
        elif "3" in temp[2]:
            ind_byes+=3
        elif "4" in temp[2]:
            ind_byes+=4
        elif "5" in temp[2]:
            ind_byes+=5
    else:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][0]+=1
    
    if f"{Current_Ball[1].strip()}" not in India_bats.keys() and temp[1]!="wide":
        India_bats[f"{Current_Ball[1].strip()}"]=[0,1,0,0,0] #[runs,ball,4s,6s,sr]
    elif "wide" in temp[1] :
        pass
    else:
        India_bats[f"{Current_Ball[1].strip()}"][1]+=1
    

    if "out" in temp[1]:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][3]+=1
        
        if "Bowled" in temp[1].split("!!")[0]:
            out_ind_bat[f"{Current_Ball[1].strip()}"]=("b" + Current_Ball[0])
        elif "Caught" in temp[1].split("!!")[0]:
            w=(temp[1].split("!!")[0]).split("by")
            out_ind_bat[f"{Current_Ball[1].strip()}"]=("c" + w[1] +" b " + Current_Ball[0])
        elif "Lbw" in temp[1].split("!!")[0]:
            out_ind_bat[f"{Current_Ball[1].strip()}"]=("lbw  b "+Current_Ball[0])

    
    
    if "no run" in temp[1] or "out" in temp[1] :
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=0
        India_bats[f"{Current_Ball[1].strip()}"][0]+=0
    elif "1 run" in temp[1]:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=1
        India_bats[f"{Current_Ball[1].strip()}"][0]+=1
    elif "2 run" in temp[1]:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=2
        India_bats[f"{Current_Ball[1].strip()}"][0]+=2
    elif "3 run" in temp[1]:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=3
        India_bats[f"{Current_Ball[1].strip()}"][0]+=3
    elif "4 run" in temp[1]:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=4
        India_bats[f"{Current_Ball[1].strip()}"][0]+=4
    elif "FOUR" in temp[1]:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=4
        India_bats[f"{Current_Ball[1].strip()}"][0]+=4
        India_bats[f"{Current_Ball[1].strip()}"][2]+=1
    elif "SIX" in temp[1]:
        Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=6
        India_bats[f"{Current_Ball[1].strip()}"][0]+=6
        India_bats[f"{Current_Ball[1].strip()}"][3]+=1
    elif "wide" in temp[1]:
        if "wides" in temp[1]:
            Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=int(temp[1][1])
            Pakistan_bowlers[f"{Current_Ball[0].strip()}"][5]+=int(temp[1][1])
        else:
            Pakistan_bowlers[f"{Current_Ball[0].strip()}"][2]+=1
            Pakistan_bowlers[f"{Current_Ball[0].strip()}"][5]+=1







#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
