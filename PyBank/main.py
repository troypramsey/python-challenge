import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, r) as csv_file:
    csvreader = csv.reader(csv_file,delimiter=',')

    csv_header = next(csvreader)