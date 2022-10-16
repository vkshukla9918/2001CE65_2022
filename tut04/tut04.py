
from datetime import datetime
start_time = datetime.now()


import pandas as pd    #importing pandas library
# try:
data = pd.read_excel("input_octant_longest_subsequence_with_range.xlsx") #reading input file
# except:
#     print("this file doesn't exist")
#     # exit()

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


longest_count = {1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0}
#for longest subsequence length
try:    
    for j, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
        temp = 0
        for i in range(len(data)-1):
            if(data.at[i,'Octact'] == data.at[i+1,'Octact'] and data.at[i,'Octact'] == int(x)):
                temp += 1
            else:
                longest_count[int(x)] = max(longest_count[int(x)],temp+1)
                temp = 0
except:
    print('error')
    exit()

            
longestoccur_count = {1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0}
#occurance of longest subsequence length
try:
    for j, x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
        temp = 0
        for i in range(len(data)-1):
            if(data.at[i,'Octact'] == data.at[i+1,'Octact'] and data.at[i,'Octact'] == int(x)):
                temp += 1
            else:
                if(temp+1 == longest_count[int(x)]):
                    longestoccur_count[int(x)] += 1
                temp = 0
except:
    print('error2')
    exit()



            


data[' '] = ' '
for j,x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
    data.at[j,'count'] = x
    data.at[j,'Longest Subsquence Length']= longest_count[int(x)]
    data.at[j,'Count'] = longestoccur_count[int(x)]

data['     '] = ''        #creating new columns
data['count '] = ''
data['longest subsequence length'] = ''
data[' count'] = ''

row  = 0
for j,x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
    data.at[row, 'count '] = x
    data.at[row, 'longest subsequence length'] = longest_count[int(x)]
    data.at[row,' count'] = longestoccur_count[int(x)]
    
    data.at[row+1, 'count '] = 'Time'
    data.at[row+1, 'longest subsequence length'] = 'From'
    data.at[row+1, ' count'] = 'To'
    row += 2  # increasing row by 2 foe time row and subsequence length count
    try:
        for i in range(len(data)):
            if data.at[i, 'Octact'] == int(x):
                initial = i #storing the row of first time range
                occurance = 0
                while(data.at[i, 'Octact'] == int(x)): #loop till the occurance of a number
                    i += 1
                    occurance += 1
                    if(i == len(data)):
                        i -= 1     #if i becomes equal to length of data then reducing it by 1 as row will start from 0.
                        break
                if occurance == longest_count[int(x)]: # if longestsubsequence length is matched then print that range of ime 
                    data.at[row, 'longest subsequence length'] = data.at[initial, 'Time']
                    data.at[row, ' count'] = data.at[i, 'Time']
                    row += 1 #shifting to next row
                occurance = 0 #making occurance again 0 to search next longest subsequence length and their range
    except:
        print('error3')
        exit()
data.to_excel("output_octant_longest_subsequence_with_range.xlsx")
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
