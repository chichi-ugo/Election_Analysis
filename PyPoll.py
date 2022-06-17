# Objectives: The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 

import csv
import os

# Assign a variable1 for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable2 to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize counter
tot_votes = 0

# Creating a list to hold the candidate options
candidate_options = []

# Declaring empty dictionary to hold candidate vote count
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percent = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read and analyze the data
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Go through each row in the CSV file
    for row in file_reader:
        # Objective 1. Increase counter by 1 for total vote count
        tot_votes += 1
        # Get candidate's name from each row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # Objective 2. Add the name to the candidate list - conditional for unique name to be added
            candidate_options.append(candidate_name)
            # Objective 4. Begin tracking each candidate's vote
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Objective 3. Calculating the percentage of votes each candidate received with for loop
for candidate_name in candidate_votes:
    # Assigning candidate vote count to a variable
    votes = candidate_votes[candidate_name]
    # Calculating the %
    vote_percent = round(float(votes) / float (tot_votes) * 100,1)
    # Print each candidate's name, vote count, and percentage of votes
    print(f"{candidate_name}:  {vote_percent:.1f}% ({votes:,})\n")

    # Objective 5. 
    # Calculate winning vote count and candidate - votes must be greater than winning count
    if (votes > winning_count) and (vote_percent > winning_percent):
        winning_count = votes
        winning_percent = vote_percent
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"------------------------------\n"
    )
print(winning_candidate_summary)


#print(candidate_votes) 
#print("Total votes: "+str(tot_votes))

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

