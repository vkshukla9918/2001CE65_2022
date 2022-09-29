import math #importing maths library
import pandas as pd #importing pandas library
data = pd.read_excel("D:\\Documents\\GitHub\\2001CE65_2022\\tut02\\input_octant_transition_identify.xlsx")
#read excel file using pandas dataframe

data.at[0,'U Avg'] = data['U'].mean()
data.at[0,'V Avg'] = data['V'].mean() 
data.at[0,'W Avg'] = data['W'].mean()

data["U'=U - U avg"] = data['U'] - data['U Avg'][0]
data["V'=V - V avg"] = data['V'] - data['V Avg'][0]  
data["W'=W - W avg"] = data['W'] - data['W Avg'][0] 

octact = [] # creating octant list

for i in range(len(data)):
#taking new variables for acessing each element of 'U','V' and 'W' Columns
    x = data["U'=U - U avg"][i]
    y = data["V'=V - V avg"][i]
    z = data["W'=W - W avg"][i]
    
    if x > 0 and y > 0 and z > 0:  #octant identification and adding to octact list,octant value of each row.
        octact.append(1)
    elif x > 0 and y > 0 and z < 0:
        octact.append(-1)                 # +, +, + = 1
    elif x < 0 and y > 0 and z > 0:       # +, +, - = -1
        octact.append(2)                  # -, +, + = 2
    elif x < 0 and y > 0 and z < 0:       # -, +, - = -2
        octact.append(-2)                 # -, -, + = 3
    elif x < 0 and y < 0 and z > 0:       # -, -, - = -3
        octact.append(3)                  # +, -, + = 4
    elif x < 0 and y < 0 and z < 0:       # +, -, - = -4
        octact.append(-3)                 
    elif x > 0 and y < 0 and z > 0:
        octact.append(4)
    elif x > 0 and y < 0 and z < 0:
        octact.append(-4)
data['Octact'] = octact.copy()        #creted new column octant and stored the value of list octant

data.at[1,''] = 'User Input'
data.at[0,' ']='Overall Count'
data.at[0,'1'] = str(octact.count(1))
data.at[0,'-1'] = str(octact.count(-1))
data.at[0,'2'] = str(octact.count(2))        #counting the values of each octant and storing the value of overall count
data.at[0,'-2'] = str(octact.count(-2))
data.at[0,'3'] = str(octact.count(3))
data.at[0,'-3'] = str(octact.count(-3))
data.at[0,'4'] = str(octact.count(4))
data.at[0,'-4'] = str(octact.count(-4))

def octact_identification(mod=5000): #function for range division and corresponding to that the value of count of an octant
    x = math.ceil(len(data)/mod)
    data.at[1,' '] = 'Mod ' + str(mod)

    i = 0
    
    for i in range(x):

        if((i+1)*mod-1) < len(data)-1:
            data.at[i+2,' '] = str((i)*mod)+'-'+str((i+1)*mod-1)
        else:
            data.at[i+2,' '] = str((i)*mod)+'-'+str(len(data)-1)
    
           
 
        data.at[i+2, '1'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod].value_counts()[1])
        data.at[i+2, '-1'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod].value_counts()[-1])
        data.at[i+2, '2'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod ].value_counts()[2])
        data.at[i+2, '-2'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod ].value_counts()[-2])
        data.at[i+2, '3'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod ].value_counts()[3])
        data.at[i+2, '-3'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod ].value_counts()[-3])
        data.at[i+2, '4'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod].value_counts()[4])
        data.at[i+2, '-4'] = str(data['Octact'].iloc[(i)*mod :(i+1)*mod].value_counts()[-4])


mod=5000        #changing variable for range
y = math.ceil(len(data)/mod)



