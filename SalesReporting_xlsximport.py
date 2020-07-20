import pandas as pd
import numpy as np
from openpyxl import load_workbook
import openpyxl

sales_data_excel = pd.ExcelFile('Demo Sales Data.xlsx')
sales_data = sales_data_excel.parse('Demo Sales Data', header=None)
sales_data.columns = ['Salesperson','Date','Revenue','Cost']
sales_data['Profit'] = sales_data['Revenue'] - sales_data['Cost']
sales_data['Margin'] = ((sales_data['Revenue'] - sales_data['Cost']) / sales_data['Revenue']) * 100
#https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column
conditions = [
    (sales_data['Margin'] < 10),
    (sales_data['Margin'] < 25),
    (sales_data['Margin'] >= 25)]
choices = [.1, .2, .3]
sales_data['Commission Percentage'] = np.select(conditions, choices, default=.15)
sales_data['Commission'] = sales_data['Profit'] * sales_data['Commission Percentage']

print(sales_data)




