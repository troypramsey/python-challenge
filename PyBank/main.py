import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file,delimiter=',')

    csv_header = next(csvreader)

    total_months = 0
    net_total = 0
    greatest_increase = 0
    greatest_increase_date = ''
    greatest_decrease = 0
    greatest_decrease_date = ''

    for row in csvreader:
        total_months += 1
        net_total += int(row[-1])
        if int(row[-1]) > greatest_increase:
            greatest_increase = int(row[-1])
            greatest_increase_date = row
        if int(row[-1]) < greatest_decrease:
            greatest_decrease = int(row[-1])
            greatest_decrease_date = row

    average_change = net_total / total_months

    print("Financial Analysis")
    print('----------------------------')
    print(f"Total Months: {total_months}")
    print(f"Total: {net_total}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Increase in Profits: {greatest_decrease_date} (${greatest_decrease})")