import pandas as pd    #importing pandas library
data = pd.read_excel("input_octant_longest_subsequence.xlsx") #reading input file

data.at[0,'U Avg'] = data['U'].mean() 
data.at[0,'V Avg'] = data['V'].mean() #average of each column
data.at[0,'W Avg'] = data['W'].mean()

data["U'=U - U avg"] = data['U'] - data['U Avg'][0]
data["V'=V - V avg"] = data['V'] - data['V Avg'][0]  #data pre processing
data["W'=W - W avg"] = data['W'] - data['W Avg'][0]

octact = [] #creating new list

for i in range(len(data)):
    x = data["U'=U - U avg"][i]
    y = data["V'=V - V avg"][i]     #created new variable
    z = data["W'=W - W avg"][i]
    
    if x > 0 and y > 0 and z > 0:
        octact.append(1)
    elif x > 0 and y > 0 and z < 0:
        octact.append(-1)                 
    elif x < 0 and y > 0 and z > 0:       
        octact.append(2)                  
    elif x < 0 and y > 0 and z < 0:       # Octant identification and appending in a list
        octact.append(-2)                 
    elif x < 0 and y < 0 and z > 0:       
        octact.append(3)                  
    elif x < 0 and y < 0 and z < 0:       
        octact.append(-3)                 
    elif x > 0 and y < 0 and z > 0:
        octact.append(4)
    elif x > 0 and y < 0 and z < 0:
        octact.append(-4)
data['Octact'] = octact.copy()  

