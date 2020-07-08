import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0
    candidates_dict = {}
    winner = 0

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates_dict:
            candidates_dict[row[2]] = 1
        else:
            candidates_dict[row[2]] += 1
            
    print(candidates_dict)
    