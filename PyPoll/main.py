# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)

input_file ="C:/Users/chara/Downloads/python-challenge/PyPoll/Resources/PyPoll.csv"
output_file ="C:/Users/chara/Downloads/python-challenge/PyPoll/analysis/election_results.txt"

# Initialize variables to track the election data

total_votes = 0
candidates ={}

# Define lists and dictionaries to track candidate names and vote counts


# Winning Candidate and Winning Count Tracker

#Read the CSV file
with open (input_file, 'r') as file:
    csvreader = csv.reader(file)

#Skip the header row
    next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
 #candidate name in the third column
        candidates[candidate] = candidates.get(candidate, 0) + 1

#Determine the winner and format results
winner = max(candidates, key=candidates.get)
results =[
     "Election Results",
     "------------------",
     f"Total votes = {total_votes}",
     "-------------------",
  ]

for candidate, votes in candidates.items():
    percentage = (votes/total_votes)*100
    results.append(f"{candidate}:{percentage:.3f}% ({votes})")

results.append("-----------")
results.append(f"Winner: {winner}")
results.append("--------------")

    #print results to terminal
for line in results:
    print(line)

    #Save results to a text file
with open(output_file, 'w')as file:
    file.write("\n".join(results))

