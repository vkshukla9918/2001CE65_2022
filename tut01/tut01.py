import math
#function for range division and corresponding to that the value of count of an octant
def octact_identification(mod=5000):
    data.at[1,'Octant ID'] = 'Mod ' + str(mod)   
    division = math.ceil(len(data)/mod)
    
    i = 0.0000
    #for loop for printing the range division
    for i in range(division):

        if((i+1)*mod-1) < len(data):
            data.at[i+2,'Octant ID'] = str((i)*mod)+'-'+str((i+1)*mod-1)
        else:
            data.at[i+2,'Octant ID'] = str((i-1)*mod)+'-'+str(len(data)-1)
    
           
    #using iloc and value_counts for count of octant in the dicided range.    
        data.at[i+2, '1'] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[1]
        data.at[i+2, '-1'] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-1]
        data.at[i+2, '2'] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[2]
        data.at[i+2, '-2'] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[-2]
        data.at[i+2, '3'] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[3]
        data.at[i+2, '-3'] = data['octant'].iloc[(i)*mod :(i+1)*mod ].value_counts()[-3]
        data.at[i+2, '4'] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[4]
        data.at[i+2, '-4'] = data['octant'].iloc[(i)*mod :(i+1)*mod].value_counts()[-4]

import pandas as pd     #imported pandas library                
data = pd.read_csv('octant_input.csv')  #reading 'octant_input.csv' file 

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

data.at[1,' '] = 'User Input'
data.at[0,'Octant ID'] = 'Overall Count'
data.at[0,'1'] = octant.count(1)
data.at[0,'-1'] = octant.count(-1)
data.at[0,'2'] = octant.count(2)         #counting the values of each octant and storing the value of overall count
data.at[0,'-2'] = octant.count(-2)
data.at[0,'3'] = octant.count(3)
data.at[0,'-3'] = octant.count(-3)
data.at[0,'4'] = octant.count(4)
data.at[0,'-4'] = octant.count(-4)

mod=5000
octact_identification(mod)   #calling function for taking ranges and in that range octant count

data.to_csv('octant_output.csv')  #printing the value to file'octant_output.csv'