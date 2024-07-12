import csv


with open('data.csv', 'r') as csv_file:
    reader_variable = csv.reader(csv_file)
    for row in reader_variable:
        print(row)