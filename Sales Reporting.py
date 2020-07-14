
import csv
import datetime

sales_data = open("Demo Sales Data.csv")
sales_table = csv.reader(sales_data)
sales_list = []

for row in sales_table:
    salesperson = str(row[0])
    date = datetime.date(row[1])
    revenue = float(row[2])
    cost = float(row[3])
    if row[0] != 'Salesperson':
        salesperson = str(row[0])
        date = datetime.date(row[1])
        revenue = float(row[2])
        cost = float(row[3])
        profit = float(row[2]) - float(row[3])
        row.append(profit)
        commission = float(profit) * .25
        row.append(commission)
        sales_list += row
    else:
        profit = 'Profit'
        row.append(profit)
        commission = 'Commission'
        row.append(commission)
        sales_list += row 
    print(row)


