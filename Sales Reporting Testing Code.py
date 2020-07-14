import csv

sales_data = open("Demo Sales Data.csv")
sales_table = csv.reader(sales_data)

for row in sales_table:
  print(row)
  