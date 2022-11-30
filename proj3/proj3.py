#https://youtu.be/0srus9mXEhk
import os
import ntpath
import glob
import pandas as pd
import numpy as np
import datetime
import streamlit as st
from pathlib import Path 
from datetime import datetime 

start_time = datetime.now() 
print(start_time.strftime("%c"))
try:
    constant_fk2d = int(st.number_input('Enter constant_fk2d'))
    multiplying_factor_3d = int(st.number_input('Enter multiplying_factor_3d'))  #taking input on webpage using streamlit
    Shear_velocity = int(st.number_input('Enter Shear_velocity'))
except:
    print('streamlit is not imported')


end_time = datetime.now()

