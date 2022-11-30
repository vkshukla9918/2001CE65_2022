import time
from datetime import datetime
start_time = datetime.now()
import streamlit as st
import numpy as np
from numpy import nan
import pandas as pd
from pathlib import Path
import math 
import openpyxl                          #imported library
from openpyxl import workbook
from openpyxl.styles import Border,Side
from openpyxl.styles import PatternFill


try:
	st.title('Welcome to Octant Batch Processing')
	uploaded_file = st.file_uploader("Choose a file",type=["xlsx"], accept_multiple_files=True)
	Mod = int(st.number_input("Enter the mod value:"))
except:
	print('strealit is not imported')


#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
