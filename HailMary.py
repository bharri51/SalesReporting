import csv
import pandas as pd
import os
import time
from datetime import datetime
import numpy
from time import mktime


sales_data_txt = open("SalesDataDemo.txt",'r')
sales_table = pd.readtable('SalesDataDemo.txt')
headers = sales_data_txt.readline()
print(headers)

sales_list = []
salesperson = ['Salesperson']
month = ['Month']
year = ['Year']
revenue = ['Revenue']
cost = ['Cost']
profit = ['Profit']
margin = ['Margin']
commission = ['Commission']

for i in sales_table():
    seeker = i.find("\t")
        
    salesperson_i = str(i[0:i.find("\t")])
    salesperson += salesperson_i

    sales_list += i
    print(i+"\n")

print(salesperson)

