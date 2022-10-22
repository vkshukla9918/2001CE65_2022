

from datetime import datetime
start_time = datetime.now()


import math # importing math library
#function for range division and corresponding to that the value of count of an octant
def octact_identification(mod=5000):
    data.at[2,'         '] = 'Mod ' + str(mod)   
    division = math.ceil(len(data)/mod)
    
    i = 0.0000
    #for loop for printing the range division
    for i in range(division):

        if((i+1)*mod-1) < len(data):
            data.at[i+3,'         '] = str((i)*mod)+'-'+str((i+1)*mod-1)
        else:
            data.at[i+3,'         '] = str((i)*mod)+'-'+str(len(data)-1)
    
           
    #using iloc and value_counts for count of octant in the dicided range.    
        data.at[i+3, ''] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[1]
        data.at[i+3, ' '] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-1]
        data.at[i+3, '  '] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[2]
        data.at[i+3, '   '] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[-2]
        data.at[i+3, '    '] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[3]
        data.at[i+3, '     '] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[-3]
        data.at[i+3, '      '] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[4]
        data.at[i+3, '       '] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-4]

import pandas as pd     #imported pandas library                
data = pd.read_excel("octant_input.xlsx")  #reading 'octant_input' file 

# using mean() taking average of U,V and W and making column in csv file
data.at[0,'U_avg'] = data['U'].mean()
data.at[0,'V_avg'] = data['V'].mean() 
data.at[0,'W_avg'] = data['W'].mean()
#data pre processing, subtracting avg of each column to each element of that column and creating new column for pre processed data
data['U-U_avg'] = data['U'] - data['U_avg'][0]
data['V-V_avg'] = data['V'] - data['V_avg'][0]  
data['W-W_avg'] = data['W'] - data['W_avg'][0]    


octant = []   # creating octant list

for i in range(len(data)):
#taking new variables for acessing each element of 'U','V' and 'W' Columns
    x = data['U-U_avg'][i]
    y = data['V-V_avg'][i]
    z = data['W-W_avg'][i]
    
    if x > 0 and y > 0 and z > 0:    #octant identification and adding to octant list,octant value of each row.
        octant.append(1)
    elif x > 0 and y > 0 and z < 0:
        octant.append(-1)                 # +, +, + = 1
    elif x < 0 and y > 0 and z > 0:       # +, +, - = -1
        octant.append(2)                  # -, +, + = 2
    elif x < 0 and y > 0 and z < 0:       # -, +, - = -2
        octant.append(-2)                 # -, -, + = 3
    elif x < 0 and y < 0 and z > 0:       # -, -, - = -3
        octant.append(3)                  # +, -, + = 4
    elif x < 0 and y < 0 and z < 0:       # +, -, - = -4
        octant.append(-3)                 
    elif x > 0 and y < 0 and z > 0:
        octant.append(4)
    elif x > 0 and y < 0 and z < 0:
        octant.append(-4)
data['octant'] = octant        #creted new column octant and stored the value of list octant




data.at[2,'        '] = 'User Input'
data.at[0,'         '] = 'Octant ID'
data.at[1,'         '] = 'Overall Count'
data.at[0,''] = '1'
data.at[0,' '] = '-1'
data.at[0,'  '] = '2'        
data.at[0,'   '] = '-2'
data.at[0,'    '] = '3'
data.at[0,'     '] = '-3'
data.at[0,'      '] = '4'
data.at[0,'       '] = '-4'
data.at[1,''] = octant.count(1)
data.at[1,' '] = octant.count(-1)
data.at[1,'  '] = octant.count(2)         #counting the values of each octant and storing the value of overall count
data.at[1,'   '] = octant.count(-2)
data.at[1,'    '] = octant.count(3)
data.at[1,'     '] = octant.count(-3)
data.at[1,'      '] = octant.count(4)
data.at[1,'       '] = octant.count(-4)

mod=5000
y = math.ceil(len(data)/mod)
octact_identification(mod)   #calling function for taking ranges and in that range octant count

data.at[0,'1'] = 'Rank1'
data.at[0,'-1'] = 'Rank2'
data.at[0,'2'] = 'Rank3'         #counting the values of each octant and storing the value of overall count
data.at[0,'-2'] = 'Rank4'
data.at[0,'3'] = 'Rank5'
data.at[0,'-3'] = 'Rank6'
data.at[0,'4'] = 'Rank7'
data.at[0,'-4'] = 'Rank8'
data.at[0,'          '] = 'Rank1 Octant ID'
data.at[0,'           '] = 'Rank1 Octant Name'


data.at[6+y,''] = 'Octant ID'
data.at[6+y,' '] = 'Octant Name'
data.at[7+y,' '] = 'Internal outward interaction'
data.at[8+y,' '] = 'External outward interaction'
data.at[9+y,' '] = 'External Ejection'
data.at[10+y,' '] = 'Internal Ejection'
data.at[11+y,' '] = 'External inward interaction'
data.at[12+y,' '] = 'Internal inward interaction'
data.at[13+y,' '] = 'Internal sweep'
data.at[14+y,' '] = 'External sweep'
data.at[6+y,'  '] = 'Count of Rank 1 Mod Values'

for j, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
    data.at[7+j+y,''] = x

overall_count = [octant.count(1),octant.count(-1),octant.count(2),octant.count(-2),octant.count(3),octant.count(-3),octant.count(4),octant.count(-4)]
#created a list of overall count of all octant.
overall_count.sort(reverse = True)  #sorting in descending order 
for j, x in enumerate(['1','-1','2','-2','3','-3','4','-4']): 
    data.at[1,x] = overall_count.index(octant.count(int(x))) + 1 #acessing and printing the count of specific octant
    if(overall_count[0] == octant.count(int(x))): #condition for highest count in sorted list highest count index would be 0
        data.at[1,'          ']= x #for highest count octant id
        if(data.at[1,'          '] == x):
            data.at[1,'           '] = data.at[7+y+j, ' '] #highest count octant ID Name




list = []
for i in range(y):   #same for mod in individual range as for overall count ranking
    mod_count = [data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[1],data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-1],data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[2],data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-2],data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[3],data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-3],data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[4],data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-4]]
    mod_count.sort(reverse = True)
    for j, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
        data.at[3+i,x] = mod_count.index(data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[int(x)]) + 1
        if(mod_count[0] == data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[int(x)]):
            data.at[3+i,'          ']= x
            list.append(int(x)) #storing octant which is ranked first in mod range
        if(data.at[3+i,'          '] == x):
            data.at[3+i,'           '] = data.at[7+y+j, ' ']


for i,x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
    data.at[7+y+i,'  '] = list.count(int(x)) #printing count of first ranked octant
    


data.to_excel("octant_output_ranking_excel.xlsx")
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))


