import math #importing maths library
import pandas as pd #importing pandas library
data = pd.read_excel("input_octant_transition_identify.xlsx")
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


data.at[8+y,'']= 'From'   #creating new columns and row for overall transition count table
data.at[5+y,' '] ='Overall Transition Count'
data.at[6+y,'1'] = 'To'
data.at[7+y,' '] = 'count'
for i, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
    data.at[8+y+i,' '] = x
    data.at[7+y,x] = x

dict = {1:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
      -1:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
       2:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},  #created nested dictionaryfor the value of transition count initial at 0
      -2:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
       3:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
      -3:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
       4:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
      -4:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0}}
        
for i in range(len(data)-1):
    dict[octact[i]][octact[i+1]] += 1
for j, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
    data.at[8+y,x] = dict[1][int(x)]
    data.at[9+y,x] = dict[-1][int(x)]
    data.at[10+y,x] =dict[2][int(x)]       
    data.at[11+y,x] =dict[-2][int(x)]    #filling the trasition count in table using loop
    data.at[12+y,x] =dict[3][int(x)]
    data.at[13+y,x] =dict[-3][int(x)]
    data.at[14+y,x] =dict[4][int(x)]
    data.at[15+y,x] =dict[-4][int(x)]

    def octant_transition_count(mod=5000):  #creating new function for mod transition count
        dict_mod = {1:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
      -1:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
       2:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
      -2:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
       3:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
      -3:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
       4:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0},
      -4:{1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0}}
        for i in range(y):
            data.at[19+y+i*13,' ']='Mod Transition Count'
            data.at[20+y+i*13,'1'] = 'To'
            data.at[21+y+i*13,' '] = 'Count'   #columns for mod transition count
            data.at[22+y+i*13,'']= 'From'
            if((i+1)*mod-1) < len(data)-1:
                data.at[20+y+i*13,' '] = str((i)*mod)+'-'+str((i+1)*mod-1)
                for j in range(i*mod,(i+1)*mod):
                    dict_mod[octact[j]][octact[j+1]] += 1
                for k, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
                    data.at[22+y+i*13,x] = dict_mod[1][int(x)]
                    data.at[23+y+i*13,x] = dict_mod[-1][int(x)]
                    data.at[24+y+i*13,x] =dict_mod[2][int(x)]
                    data.at[25+y+i*13,x] =dict_mod[-2][int(x)] #fillimg the table upto second last range for transition count
                    data.at[26+y+i*13,x] =dict_mod[3][int(x)]
                    data.at[27+y+i*13,x] =dict_mod[-3][int(x)]
                    data.at[28+y+i*13,x] =dict_mod[4][int(x)]
                    data.at[29+y+i*13,x] =dict_mod[-4][int(x)]
                    dict_mod[1][int(x)] = 0
                    dict_mod[-1][int(x)] = 0
                    dict_mod[2][int(x)] = 0
                    dict_mod[-2][int(x)] = 0  #making here again all  0
                    dict_mod[3][int(x)] = 0
                    dict_mod[-3][int(x)] = 0
                    dict_mod[4][int(x)] = 0
                    dict_mod[-4][int(x)] = 0

                
        
            else:
                data.at[20+y+i*13,' '] = str((i)*mod)+'-'+str(len(data)-1)
                for j in range(i*mod,len(data)-1):
                    dict_mod[octact[j]][octact[j+1]] += 1
                for j, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
                    data.at[22+y+i*13,x] = dict_mod[1][int(x)]
                    data.at[23+y+i*13,x] = dict_mod[-1][int(x)]
                    data.at[24+y+i*13,x] =dict_mod[2][int(x)]
                    data.at[25+y+i*13,x] =dict_mod[-2][int(x)]
                    data.at[26+y+i*13,x] =dict_mod[3][int(x)]       #for lat range which would not be of 5000 length
                    data.at[27+y+i*13,x] =dict_mod[-3][int(x)]
                    data.at[28+y+i*13,x] =dict_mod[4][int(x)]
                    data.at[29+y+i*13,x] =dict_mod[-4][int(x)]
        
    
    
            for j,x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
                data.at[22+y+j+i*13,' '] = x
                data.at[21+y+i*13,x] = x
octact_identification(mod)
octant_transition_count(mod)    #calling functions

data.to_excel("output_octant_transition_identify.xlsx") #printing output in excel file

        