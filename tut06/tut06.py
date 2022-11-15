from datetime import datetime
start_time = datetime.now()
import pandas as pd
from numpy import NaN
import csv                    # imported libraries
import openpyxl
# reading both the files
data_attendance = pd.read_csv("input_attendance.csv")
data_registered_students = pd.read_csv("input_registered_students.csv")

data_attendance['Roll']=''
data_attendance['Name']=''
N = len(data_attendance) 
rows = 0
for i in range(0,N):
    a = data_attendance['Attendance'][i]   
    if(type(a)==str):
        b = a[0:8]      # Storing roll number 
        c = a[9:]       # storing name 
        data_attendance['Roll'][i]=b 
        data_attendance['Name'][i]=c
    else:
        rows+=1
        data_attendance['Roll'][i]= NaN
        data_attendance['Name'][i]= NaN

data_attendance.drop('Attendance',inplace=True,axis=1)
attendance_days =  {}  
total_days = {}
data_attendance['Date']=''    #column of date and time
data_attendance['Time']=''
for i in range(0,N):
    time_stamp = pd.to_datetime(data_attendance['Timestamp'][i],format = "%d-%m-%Y %H:%M")
    data_attendance['Date'][i]=time_stamp.date()
    data_attendance['Time'][i]=time_stamp.time()  #filling with date, time and time stamp
    data_attendance['Timestamp'][i]=time_stamp
for j in range(0,N):
    start_date = data_attendance['Timestamp'][j]
    break
for k in range(0,N):
    last_date = data_attendance['Timestamp'][k]  

while(start_date.date()<=last_date.date()):
    if(start_date.day_name()=="Monday" or start_date.day_name()=='Thursday'):
        attendance_days[start_date.date()]=1           # attendance day as per scheduled class
        total_days[start_date.date()]=1
    else:
        total_days[start_date.date()]=0
    start_date = start_date + pd.DateOffset(days=1)
new_data = data_attendance.sort_values(by=['Roll','Date','Time'])  #sorted based on roll no. then date and time
new_data = new_data.reset_index()
new_data.drop('index',inplace=True,axis=1)
new_data.drop('Timestamp',inplace=True,axis=1)   #removing columns

dates = []
dict_dates = {}
count = 1
for i in attendance_days:
    dates.append(i)
    dict_dates[i]=count
    count+=1
for j in range(0,len(dates)):
    data_registered_students['Date '+str(j+1)]='A'
data_registered_students['Actual Lecture Taken']=''
data_registered_students['Total Real']=''
data_registered_students['Attendance%']=''   #new columns

present_row = 0
for i in range(0,len(data_registered_students)):
    x = data_registered_students['Roll No'][i]
    stud_data = pd.DataFrame(columns = ['Date','Roll','Name','Total Attendance Count','Real','Duplicate','Invalid','Absent']) # new dataframe with new required columns
    dicts = {'Date':'','Roll':x,'Name':data_registered_students['Name'][i],'Total Attendance Count':0,'Real':0,'Duplicate':0,'Invalid':0,'Absent':0}
    #dictionnary to store the data of each studnts
    row_data = pd.DataFrame(dicts,index = [0])
    stud_data = pd.concat([stud_data,row_data],ignore_index = True)
    dict_fake = {}
    dict_present = {}
      

    for j in range(0,len(dates)):
        dict_fake[dates[j]]=0
        dict_present[dates[j]]=0
    for k in range(present_row,len(new_data)):
        y = new_data['Roll'][k]
        if(type(y)==float):
            break
        if(x<y):
            present_row=k
            break
        else :
            if(total_days[new_data['Date'][k]]==1 and  str(new_data['Time'][k])>='14:00:00' and str(new_data['Time'][k])<='15:00:00'):
                data_registered_students["Date "+ str(dict_dates[new_data['Date'][k]])][i]='P'
                dict_present[new_data['Date'][k]]+=1
            elif(total_days[new_data['Date'][k]]==1):
                dict_fake[new_data['Date'][k]]+=1
    presents_no = 0
    for l in range(0,len(dates)):
        if data_registered_students['Date '+str(l+1)][i]=='P':
            presents_no+=1
    data_registered_students['Actual Lecture Taken'][i]=len(dates)
    data_registered_students['Total Real'][i]= presents_no
    data_registered_students['Attendance%'][i]=round((presents_no/len(dates))*100,2)
    
    for i in range(1,len(dates)+1):
        attendance = {}
        attendance['Date'] = "Date " + str(i)
        if (dict_present[dates[i-1]]>0):
            attendance['Real'] = 1
        else:
            attendance['Real'] = 0
        if (dict_present[dates[i-1]]>0):
            attendance['Duplicate'] = dict_present[dates[i-1]]-1
        else:
            attendance['Duplicate'] = 0
        attendance['Invalid'] = dict_fake[dates[i-1]]
        if (dict_present[dates[i-1]]>0):
            attendance['Absent'] = 0
        else:
            attendance['Absent'] = 1
        attendance['Total Attendance Count'] = attendance['Real']+attendance['Duplicate']+attendance['Invalid']
        data = pd.DataFrame(attendance,index=[0])
        stud_data = pd.concat([stud_data,data],ignore_index=True)
    for j in range(1,len(dates)+1):
        stud_data.loc[0,'Total Attendance Count'] += stud_data.loc[j,'Total Attendance Count']
        stud_data.loc[0,'Real'] += stud_data.loc[j,'Real']
        stud_data.loc[0,'Duplicate'] += stud_data.loc[j,'Duplicate']  #printed attendance corresponding to each student in respective date and column
        stud_data.loc[0,'Invalid'] += stud_data.loc[j,'Invalid']
        stud_data.loc[0,'Absent'] += stud_data.loc[j,'Absent']
    stud_data.to_excel("output\\"+  str(x) + ".xlsx",index=False)#for each student data that is in number 221

data_registered_students.to_excel("output\\attendance_report_consolidated.xlsx", index = False)

#printing consolidated attendance report



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
