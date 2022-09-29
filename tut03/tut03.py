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

max1=[]
max_1=[]
max2=[]      #created empty list
max_2=[] 
max3= []
max_3=[]
max4=[]
max_4 = []

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
x = len(data)
for i in range(x-1):  #appending subsequences of a octant
    if (octact[i] == 1 and octact[i+1] == 1):
        a += 1
    elif((octact[i-1]!= 1 and octact[i] == 1 and octact[i+1] != 1) or (octact[0] == 1 and octact[1]!= 1)or (octact[x-2] != 1 and octact[x-1] == 1)):
        max1.append(1)
    else:
        if a>0:
            max1.append(a+1)
            a = 0
    if(octact[i] == -1 and octact[i+1] == -1):
        b += 1
    elif((octact[i-1]!= -1 and octact[i] == -1 and octact[i+1] != -1) or (i== 0 and octact[0] == -1 and octact[1]!= -1)or (octact[x-2] != -1 and octact[x-1] == -1)):
        max_1.append(1)
    else:
        if b>0:
            max_1.append(b+1)
            b = 0
    if(octact[i] == 2 and octact[i+1] == 2):
        c += 1
    elif((octact[i-1]!= 2 and octact[i] == 2 and octact[i+1] != 2) or (i== 0 and octact[0] == 2 and octact[1]!= 2)or (octact[x-2] != 2 and octact[x-1] == 2)):
        max2.append(1)
    else:
        if c>0:
            max2.append(c+1)
            c = 0
    if(octact[i] == -2 and octact[i+1] == -2):
        d += 1
    elif((octact[i-1]!= -2 and octact[i] == -2 and octact[i+1] != -2) or (i== 0 and octact[0] == -2 and octact[1]!= -2)or (octact[x-2] != -2 and octact[x-1] == -2)):
        max_2.append(1)
    else:
        if d>0:
            max_2.append(d+1)
            d = 0
    if(octact[i] == 3 and octact[i+1] == 3):
        e += 1
    elif((octact[i-1]!= 3 and octact[i] == 3 and octact[i+1] != 3) or (i== 0 and octact[0] == 3 and octact[1]!= 3)or (octact[x-2] != 3 and octact[x-1] == 3)):
        max3.append(1)
    else:
        if e>0:
            max3.append(e+1)
            e = 0
    if(octact[i] == -3 and octact[i+1] == -3):
        f += 1
    elif((octact[i-1]!= -3 and octact[i] == -3 and octact[i+1] != -3) or (i== 0 and octact[0] == -3 and octact[1]!= -3)or (octact[x-2] != -3 and octact[x-1] == -3)):
        max_3.append(1)
    else:
        if f>0:
            max_3.append(f+1)
            f = 0
    if(octact[i] == 4 and octact[i+1] == 4):
        g += 1
    elif((octact[i-1]!= 4 and octact[i] == 4 and octact[i+1] != 4) or (i== 0 and octact[0] == 4 and octact[1]!= 4)or (octact[x-2] != 4 and octact[x-1] == 4)):
        max4.append(1)
    else:
        if g>0:
            max4.append(g+1)
            g = 0
    if(octact[i] == -4 and octact[i+1] == -4):
        h += 1
    elif((octact[i-1]!= -4 and octact[i] == -4 and octact[i+1] != -4) or (i== 0 and octact[0] == -4 and octact[1]!= -4)or (octact[x-2] != -4 and octact[x-1] == -4)):
        max_4.append(1)
    else:
        if h>0:
            max_4.append(h+1)
            h = 0

data[' '] = ' '
for j,x in enumerate(['1','-1','2','-2','3','-3','4','-4']):
    data.at[j,'count'] = x
data['Longest Subsquence Length'] = ' '
data['Count'] = ' '

data.at[0,'Longest Subsquence Length'] = max(max1)
data.at[0,'Count'] = max1.count(max(max1))
data.at[1,'Longest Subsquence Length'] = max(max_1)
data.at[1,'Count'] = max_1.count(max(max_1))
data.at[2,'Longest Subsquence Length'] = max(max2)
data.at[2,'Count'] = max2.count(max(max2))
data.at[3,'Longest Subsquence Length'] = max(max_2) #filling table (max subsequence length and its no. of occurance)
data.at[3,'Count'] = max_2.count(max(max_2))
data.at[4,'Longest Subsquence Length'] = max(max3)
data.at[4,'Count'] = max3.count(max(max3))
data.at[5,'Longest Subsquence Length'] = max(max_3)
data.at[5,'Count'] = max_3.count(max(max_3))
data.at[6,'Longest Subsquence Length'] = max(max4)
data.at[6,'Count'] = max4.count(max(max4))
data.at[7,'Longest Subsquence Length'] = max(max_4)
data.at[7,'Count'] = max_4.count(max(max_4))


data.to_excel("output_octant_longest_subsequence.xlsx")
