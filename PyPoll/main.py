#Calculate The total number of votes cast
#Create A complete list of candidates who received votes
#calculate The percentage of votes each candidate won
#calculate The total number of votes each candidate won
#The winner of the election based on popular vote.

import csv
import os

filepath= os.path.join("Resources\election_data.csv")

with open(filepath,'r') as csvfile:
    csvreader= csv.reader(csvfile, delimeter= ',')
    next(csvreader, None)

#empty lists to collect county and candidates in the list
candidate= []
county=[]
voterID= []

#variables to keep track of
number_votes= len(voterID)
candidate_win= []

for row in csvreader:
    vote= row[0]
    votecandidate= str [row[2]]
    candidate.append(votecandidate)