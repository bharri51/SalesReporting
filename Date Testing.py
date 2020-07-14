
import csv
import datetime

sales_data = open("Demo Sales Data.csv")
sales_table = csv.reader(sales_data)
sales_list = []

for row in sales_table(2):
    salesperson = str(row[0])
    date_time_str = row[1]

    if row[0] != 'Salesperson':
        date_time_obj = datetime.datetime.strptime(date_time_str, '%m/%d/%Y')
        date = date_time_obj.date()
    print(row)



