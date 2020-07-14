import csv

with open('Demo Sales Data.csv') as sales_data:
    mather_manipulator = csv.writer(sales_data)
    mather_manipulator.writerow(['Revenue']-['Cost'])


    sales_table = csv.reader(sales_data)
