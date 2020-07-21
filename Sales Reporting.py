
import csv
import datetime
import os
import time
from datetime import datetime
import numpy
from time import mktime
import re
import urllib


sales_data_txt = open("Demo Sales Data.csv", 'r')
sales_table = sales_data_txt.read()
print(sales_table)
headers = sales_table.readline()
sales_list = []

for row in sales_data:
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


