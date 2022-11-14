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
        attendance_days[start_date.date()]=1
        total_days[start_date.date()]=1
    else:
        total_days[start_date.date()]=0
    start_date = start_date + pd.DateOffset(days=1)






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
