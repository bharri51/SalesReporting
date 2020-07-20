import csv
import xlsx
import pandas as pd
import os
import time
from datetime import datetime
import numpy
from time import mktime


sales_data_excel = pd.ExcelFile('Demo Sales Data.xlsx')
  
# View the excel_file's sheet names 
print(sales_data_excel.sheet_names) 
  
# Load the excel_file's Sheet1 as a dataframe 
sheet1 = excel_file.parse('Sheet1') 
print(sheet1) 



