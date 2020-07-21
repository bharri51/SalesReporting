import pandas as pd
import numpy as np
from openpyxl import load_workbook
import openpyxl

sales_data_excel = pd.ExcelFile('Demo Sales Data.xlsx')
sales_data = sales_data_excel.parse('Demo Sales Data', header=None)
sales_data.columns = ['Salesperson','Date','Revenue','Cost']
sales_data['Profit'] = sales_data['Revenue'] - sales_data['Cost']
sales_data['Margin'] = ((sales_data['Revenue'] - sales_data['Cost']) / sales_data['Revenue']) * 100
conditions = [
    (sales_data['Margin'] < 10),
    (sales_data['Margin'] < 25),
    (sales_data['Margin'] >= 25)]
choices = [.1, .2, .3]
sales_data['Commission Percentage'] = np.select(conditions, choices, default=.15)
sales_data['Commission'] = sales_data['Profit'] * sales_data['Commission Percentage']

print(sales_data,"\n\n")

grouped_sales_data = sales_data.groupby('Salesperson').agg({'Revenue':"sum", 'Cost':"sum",'Profit':"sum",'Margin':"mean",'Commission':"sum"})

print(grouped_sales_data)



