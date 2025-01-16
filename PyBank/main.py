# Import necessary modules
import os
import csv

# File path to the dataset

file_path = "C:/Users/chara/Downloads/python-challenge/PyBank/Resources/budget_data.csv"

# Initialize variables

total_months = 0
total_net = 0
previous_profit = None
changes = []
dates = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]


# Read the CSV file

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    for row in csv_reader:

        # Skip empty rows

        if len(row) < 2:
            continue

        try:
            # Extract date and profit/loss
            date = row[0]
            profit = int(row[1])

            # Increment total months
            total_months += 1

            # Add to total net amount

            total_net += profit

            # Calculate the change in profit/loss (if not the first row)

            if previous_profit is not None:
                change = profit - previous_profit
                changes.append(change)
                dates.append(date)

                # Check for greatest increase

                if change > greatest_increase[1]:
                    greatest_increase = [date, change]

                # Check for greatest decrease
                if change < greatest_decrease[1]:
                    greatest_decrease = [date, change]

            # Update previous profit
            previous_profit = profit
#printing for Skipping row with invalid data
        except ValueError:
            print(f"Skipping row with invalid data: {row}")

# Debugging Step: Print changes list to verify

print(f"Changes: {changes}")

# Calculate the average change

if changes:  # Ensure changes list is not empty
    average_change = sum(changes) / len(changes)
else:
    average_change = 0  # Set to 0 if there are no changes

# Format the results
output = (

    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
# Print to terminal
print(output)

# Export the results to a text file

output_path = os.path.join("C:/Users/chara/Downloads/python-challenge/PyBank/analysis", "budget_analysis.txt")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, mode='w') as output_file:
    output_file.write(output)
 #Export the results to a text file

output_path = os.path.join("C:/Users/chara/Downloads/python-challenge/PyBank/analysis", "budget_analysis.txt")



# Ensure the folder exists

os.makedirs(os.path.dirname(output_path), exist_ok=True)



# Write the output to the file

with open(output_path, mode='w') as output_file:

    output_file.write(output)



print(f"Analysis exported to {output_path}")
