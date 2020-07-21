import csv
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
sheet1 = sales_data_excel.parse('Demo Sales Data') 
print(sheet1) 

sales_table = sales_data_txt.read()
print(sales_table)
headers = sales_data_txt.readline()
sales_list = []

for row in sales_data_txt:
    salesperson = str(row[0])
    month_year = row[1] + " " + row[2]
    revenue = float(row[3])
    cost = float(row[4] * 1.01)
    profit = float(row[3]) - float(row[4])
    row.append(profit)
    commission = float(profit) * .25
    row.append(commission)
    sales_list += row
    print(row)


