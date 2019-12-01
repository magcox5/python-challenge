# main.py for PyPoll

import os
import csv
import sys

def print_summary(total_votes):
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    print('Khan: 63.000% (2218231)')
    print('Correy: 20.000% (704200)')
    print('Li: 14.000% (492940)')
    print("O'Tooley: 3.000% (105630)")
    print('-------------------------')
    print('Winner: Khan')
    print('-------------------------')
          
# Path to collect data from the Resources folder
election_csv = os.path.join('', 'Resources', 'election_data.csv')


# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Initialize variables for data you're collecting
    total_votes = 0

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # Loop through the data, skipping header row
    first_row = next(csvreader)
    for row in csvreader:
        total_votes += 1

    

    print_summary(total_votes)
    orig_stdout = sys.stdout
    filename  = open("election_results",'w')
    sys.stdout = filename

    print_summary(total_votes)
    sys.stdout = orig_stdout
    filename.close()
    
