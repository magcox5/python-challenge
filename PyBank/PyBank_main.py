# PyBank_main.py for PyBank
import os
import csv
import datetime
import sys

# Function to print out budget summary
def print_summary(total_months, total_profit, avg_change, greatest_increase_profit, greatest_decrease_profit):
    print("Financial Analysis")
    print("-----------------------------------------------------")
    print(f"Total Months:  {total_months}")
    print(f"Total:  ${total_profit :,.2f}")
    print(f"Average Change: ${(sum_profit_change/(total_months-1)): ,.2f}")
    print(f"Greatest Profit Increase: {greatest_increase_month} ${greatest_increase_profit:,.2f}")
    print(f"Greatest Profit Decrease: {greatest_decrease_month} ${greatest_decrease_profit:,.2f}")


# Path to collect data from the Resources folder
budget_csv = os.path.join('', 'Resources', 'budget_data.csv')

# Set output file name
output_file = "budget_summary.txt"

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Initialize variables for data you're collecting
    total_months = 0
    total_profit = 0.0
    average_profit_change = 0.0
    greatest_increase_profit = 0.0
    greatest_decrease_profit = 0.0

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    greatest_increase_month = datetime.date(2000, 1, 1)
    greatest_decrease_month = datetime.date(2000, 1, 1)
    last_row = 0.0
    sum_profit_change = 0.0
    
    # Loop through the data, skipping header row
    first_row = next(csvreader)
    for row in csvreader:

        total_months += 1
        total_profit = total_profit + float(row[1])

        # test to see if difference between current and last
        # row profit is greater than previous increase/decrease profit value
        # save the greatest increase/decrease change in profit
        if total_months <= 1:
            last_row = float(row[1])
        if total_months > 1:
            row_difference = float(row[1]) - last_row
            if row_difference > greatest_increase_profit:
                greatest_increase_profit = row_difference
                greatest_increase_month = row[0]
            elif row_difference < greatest_decrease_profit:
                greatest_decrease_profit = row_difference
                greatest_decrease_month = row[0]

            last_row = float(row[1])
            sum_profit_change = sum_profit_change + row_difference
            
    # Calculate average profit/loss change
    avg_change = sum_profit_change/(total_months-1)
    
    # Write summary data to screen
    print_summary(total_months, total_profit, avg_change, greatest_increase_profit, greatest_decrease_profit)

    # Save current standard output, then set output to a file
    orig_stdout = sys.stdout
    filename  = open(output_file,'w')
    sys.stdout = filename

    # Write summary data to txt file
    print_summary(total_months, total_profit, avg_change, greatest_increase_profit, greatest_decrease_profit)

    # Reset output to screen
    sys.stdout = orig_stdout
    filename.close()
    

    
        

        
        
