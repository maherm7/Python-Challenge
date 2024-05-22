import os
import csv

#locating the file 
results = os.path.join("PyPoll", "analysis", "results.txt")
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

#declaring values
total_votes = 0
candidates = []
candidate_perc_votes_won = {}
candidates_votes = {}
winner_of_election = ""

#Opening the csv file as a reader
with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    previous_candidate = 0

#Loop through the rows to find total votes
    for row in csv_reader:
        total_votes +=1
        candidate = row[2]

#Loop to find the candidates in the election       
        if candidate not in candidates:
            candidates.append(candidate)
            candidates_votes[candidate] = 1
        else:
            candidates_votes[candidate] += 1

#Calculates the % of votes each candidate won
for candidate in candidates:
    candidate_perc_votes_won[candidate] = round((candidates_votes[candidate] / total_votes) * 100, 3)

# Determines the winner of the election
winner_of_election = max(candidates_votes, key=candidates_votes.get)

# Print the results
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_perc_votes_won[candidate]}% ({candidates_votes[candidate]})")
print("---------------------------------")
print(f"Winner: {winner_of_election}")
print("---------------------------------")   


# Write the results to a text file
with open(results, "w") as file:
    file.write("Election Results\n")
    file.write("---------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("---------------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {candidate_perc_votes_won[candidate]}% ({candidates_votes[candidate]})\n")
    file.write("---------------------------------\n")
    file.write(f"Winner: {winner_of_election}\n")
    file.write("---------------------------------\n")