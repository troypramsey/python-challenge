import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0
    candidates_dict = {}
    winner = 0
    winner_name = ''

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates_dict:
            candidates_dict[row[2]] = 1
        else:
            candidates_dict[row[2]] += 1

        if candidates_dict[row[2]] > winner:
            winner = candidates_dict[row[2]]

    for key, value in candidates_dict.items():
        if value == winner:
            winner_name = str(key)
            
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------")
    for key, value in candidates_dict.items():
        print(f"{key}: {round(value/total_votes * 100, 2)}% ({value})")
    print("---------------------")
    print(f"Winner: {winner_name}")
    print("---------------------")
    