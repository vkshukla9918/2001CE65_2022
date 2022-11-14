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







#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
