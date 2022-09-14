# def octact_identification(mod=5000):
###Code
# mod=5000
# octact_identification(mod)
import pandas as pd                     #imported pandas library
data = pd.read_csv('octant_input.csv')  #reading 'octant_input.csv' file 

data.at[0,'U_avg'] = data['U'].mean()
data.at[0,'V_avg'] = data['V'].mean() # using mean() taking average of U,V and W and making column in csv file
data.at[0,'W_avg'] = data['W'].mean()

data['U-U_avg'] = data['U'] - data['U_avg'][0]
data['V-V_avg'] = data['V'] - data['V_avg'][0]  
data['W-W_avg'] = data['W'] - data['W_avg'][0]    

#data pre processing, subtracting avg of each column to each element of that column and 
# creating new column for pre processed data
octant = []   # creating octant emptylist

for i in range(len(data)):
    x = data['U-U_avg'][i]
    y = data['V-V_avg'][i]
    z = data['W-W_avg'][i]
    
    if x > 0 and y > 0 and z > 0:    #octant identification and adding to octant list,octant value of each row.
        octant.append(1)
    elif x > 0 and y > 0 and z < 0:
        octant.append(-1)
    elif x < 0 and y > 0 and z > 0:
        octant.append(2)
    elif x < 0 and y > 0 and z < 0:
        octant.append(-2)
    elif x < 0 and y < 0 and z > 0:
        octant.append(3)
    elif x < 0 and y < 0 and z < 0:
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

data.to_csv('octant_output1.csv')