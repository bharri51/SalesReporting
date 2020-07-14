import csv

<<<<<<< Updated upstream
sales_data = open("Demo Sales Data.csv")
sales_table = csv.reader(sales_data)
=======
with open('Demo Sales Data.csv') as sales_data:
    fieldnames = ['Salesperson','Date','Revenue','Cost']
    mather_manipulator = csv.writer(sales_data)
    mather_manipulator.writerow(['Revenue'] - ['Cost'],delimiter=' ', quoting=csv.QUOTE_NONE)



>>>>>>> Stashed changes

for row in sales_table:
  print(row)
  