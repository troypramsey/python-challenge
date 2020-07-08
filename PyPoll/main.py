# Importing modules for reading and writing csv files
import os
import csv
import sys

# Initializing path variable
csv_path = os.path.join("Resources", "election_data.csv")

# Converting path variable to readable csv format
with open(csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    # Passing over initial header row
    csv_header = next(csvreader)

    # Initializing global variables
    total_votes = 0
    candidates_dict = {}
    winner = 0
    winner_name = ''

    # Iterates through each row
    for row in csvreader:
        # Incrementing Total Votes
        total_votes += 1
        # Populates dictionary with new candidate as key and sets initial key value as 1
        if row[2] not in candidates_dict:
            candidates_dict[row[2]] = 1
        # Increments each candidate's vote count
        else:
            candidates_dict[row[2]] += 1
        # Increments winner variable
        if candidates_dict[row[2]] > winner:
            winner = candidates_dict[row[2]]
    # Iterates over candidate dictionary to assign the winner's key to a string variable
    for key, value in candidates_dict.items():
        if value == winner:
            winner_name = str(key)

    # Create a function to write the results
    def results():
        print("Election Results")
        print("---------------------")
        print(f"Total Votes: {total_votes}")
        print("---------------------")
        # Iterates over candidate names and votes received and prints them to individual f-strings
        for key, value in candidates_dict.items():
            print(f"{key}: {round(value/total_votes * 100, 2)}% ({value})")
        print("---------------------")
        print(f"Winner: {winner_name}")
        print("---------------------")
        
    # Print the results to the terminal
    print(results())
    
    # Outputs results to election_results.txt file
    sys.stdout = open("election_results.txt", 'w')
    print(results())
    sys.stdout.close()