# Importing modules
import os
import csv

# Initializing path object
csv_path = os.path.join("Resources", "budget_data.csv")

# Converting path object to readable file
with open(csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file,delimiter=',')

    # Skipping over csv header
    csv_header = next(csvreader)

    # Initializing global variables
    total_months = 0
    net_total = 0
    change = 0
    greatest_increase = 0
    greatest_increase_date = ''
    greatest_decrease = 0
    greatest_decrease_date = ''
    amounts_lst = []
    change_lst = []

    # Iterating through each row in the csv
    for row in csvreader:
        
        # Incrementing Total Months
        total_months += 1
        
        # Incrementing End Total
        net_total += int(row[1])
        
        # Using a list to keep track of previous changes
        amounts_lst.append(int(row[1]))
        
        # Calculating the change between current row and previous row
        if len(amounts_lst) < 2:
            continue
        else:
            change = amounts_lst[-1] - amounts_lst[-2]
            change_lst.append(change)
        
        # Incrementing Greatest Increase In Profits
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]
        
        # Incrementing Greatest Decrease In Profits
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]
        
        # Keeping list at two items to maximize memory
        if len(amounts_lst) > 2:
            amounts_lst.pop(0)

    # Calculating Average Change
    average_change = round((sum(change_lst) / len(change_lst)), 2)

    # Assigning the final analysis to a variable
    analysis = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
    )

    # Printing the analysis to the terminal
    print(analysis)

    # Creating path variable for different operating systems
    analysis_path = os.path.join('Analysis', 'budget_analysis.txt')

    # Writing the analysis to an external .txt
    with open(analysis_path, 'w') as file:
        file.write(analysis)
