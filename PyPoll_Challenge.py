# Objectives: 
# 1. 1. Calculate the voter turnout for each county.
# 2. Calculate the percentage of votes from each county and the total count.
# 3. Find the county with the highest turnout.
# --------------------------------------------------------  

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

# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percent = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
county_voter_turnout = 0
county_winning_percent = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read and analyze the data
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Go through each row in the CSV file
    for row in file_reader:
        # Increase counter by 1 for total vote count
        tot_votes += 1
        # Get candidate's name from each row
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]

        # Add the name to the candidate list - conditional for unique name to be added
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begin tracking each candidate's vote
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in counties:
            # 4b: Add the existing county to the list of counties.
            counties.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Saving the results in our txt file
with open(file_to_save, "w") as txt_file:

    # Print the election results: total vote count
    election_results = (
        f"\n *** Election Results ***\n"
        f"-------------------------\n"
        f"Total Votes: {tot_votes:,}\n"
        f"-------------------------\n"
        " * County Votes: * \n"
        )
    print(election_results, end="")
    # Save to the txt file
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in counties:
        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percent = round(float(county_vote_count) / float(tot_votes) * 100,1)
         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_vote_percent:.1f}% ({county_vote_count:,})\n")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote_count > county_voter_turnout) and (county_vote_percent > county_winning_percent):
            county_voter_turnout = county_vote_count
            largest_county = county_name
            county_winning_percent = county_vote_percent

    # 7: Print the county with the largest turnout to the terminal.
    county_turnout_summary = (
        f"---------------------------------\n"
        f"County with the largest turnout: {largest_county}\n"
        f"{largest_county} had a total of {county_voter_turnout:,} votes ({county_winning_percent:.1f}% of total votes)\n"
        f"---------------------------------\n"
        " * Candidates: *\n"
        )
    print(county_turnout_summary)
        
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_turnout_summary)

    # Calculating the percentage of votes each candidate received with for loop
    for candidate_name in candidate_votes:
        # Assigning candidate vote count to a variable
        votes = candidate_votes[candidate_name]
        # Calculating the %
        vote_percent = round(float(votes) / float (tot_votes) * 100,1)
        # Assigning each candidate's name, vote count, and percentage of votes to a variable and printing
        candidate_results = (f"{candidate_name}:  {vote_percent:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Saving the results to the txt file
        txt_file.write(candidate_results)

        # Calculate winning vote count and candidate - votes must be greater than winning count
        if (votes > winning_count) and (vote_percent > winning_percent):
            winning_count = votes
            winning_percent = vote_percent
            winning_candidate = candidate_name
    # Printing the winning candidate results to terminal
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"------------------------------\n"
        )
    print(winning_candidate_summary)
    # Save the winner result summary to txt file
    txt_file.write(winning_candidate_summary)
