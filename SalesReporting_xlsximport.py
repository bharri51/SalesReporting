import csv
import pandas as pd
import os
import time
from datetime import datetime
import numpy
from time import mktime
import json
from openpyxl import load_workbook
import openpyxl
import dateutil



sales_data_excel = pd.ExcelFile('Demo Sales Data.xlsx')
sales_data = sales_data_excel.parse('Demo Sales Data', header=None)
sales_data.columns = ['Salesperson','Date','Revenue','Cost']
sales_data['Profit'] = sales_data['Revenue'] - sales_data['Cost']
sales_data['Margin'] = ((sales_data['Revenue'] - sales_data['Cost']) / sales_data['Revenue']) * 100
sales_data['Commission'] = sales_data['Profit'] * .25
print(sales_data)




