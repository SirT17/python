import os
import csv

csvpath = os.path.join("Resources", "Election_data.csv")

with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    Candidates = {}
    vote_count = 0
    VoteID = []
    candidates = []

    for row in csvreader:
        vote_count += 1
        if row[2] not in Candidates:
            Candidates[row[2]] = 1
        if row[2] in Candidates:
            Candidates[row[2]] += 1

winner = ['name',0]

for name in Candidates:
    if Candidates[name] > winner[1]:
        winner[0]= name
        winner[1]= Candidates[name]
print (f'Election Results \n----------------- \nTotalVotes: {vote_count} \n---------------------')
print (f'{Candidates} ')
print(f'---------------------------\nWinner: {winner[0]} \n-----------------------')