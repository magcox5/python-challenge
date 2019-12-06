# main.py for PyPoll

import os
import csv
import sys
import operator

# Function to print poll summary
def print_summary(total_votes, candidate_results):

    sorted_results = sorted(candidate_results.items(), key=operator.itemgetter(1), reverse=True)
    sorted_candidates = sorted(candidate_results, key=candidate_results.get, reverse=True)
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes:,}')
    print('-------------------------')

    for candidate in sorted_results:
      candidate_name = candidate[0]
      candidate_pct = (candidate[1]/total_votes)*100
      candidate_votes = candidate[1]
      print(f'{candidate_name}:  {candidate_pct:.3f}% ({candidate_votes:,})')
      
    print('-------------------------')
    print(f'Winner: {sorted_candidates[0]}')
    print('-------------------------')
          
# Path to collect data from the Resources folder
election_csv = os.path.join('', 'Resources', 'election_data.csv')

# Variable to hold name of output file
output_file = "election_results.txt"

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Initialize variables for data you're collecting
    total_votes = 0

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Create dictionary to hold candidates names and number of votes received
    candidate_results = {}
    
    # Loop through the data, skipping header row
    # Count up total votes, and votes for each candidate
    first_row = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidate_results:
          candidate_results[candidate_name] = candidate_results[candidate_name] + 1
        else:
          candidate_results[candidate_name] = 1

    
    # Print results to screen
    print_summary(total_votes, candidate_results)
    
    # Set standard output to a file, then print results to file
    orig_stdout = sys.stdout
    filename  = open(output_file,'w')
    sys.stdout = filename
    print_summary(total_votes,candidate_results)

    # Reset output to screen, and close results file
    sys.stdout = orig_stdout
    filename.close()
    
