from datetime import datetime
start_time = datetime.now()
import pandas as pd
import csv                    # imported libraries
import openpyxl
# reading both the files
data_attendance = pd.read_csv("input_attendance.csv")
data_registered_students = pd.read_csv("input_registered_students.csv")







#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
