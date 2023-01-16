import os
import csv

votes_list=[]

candidate_list = []

candidate = ''

election_data_csv = os.path.join('Resources', 'election_data.csv')

with open(election_data_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
        votes_list.append(row[2])
        if row[2] != candidate and candidate_list.count(row[2])==0:
            candidate_list.append(row[2])
            candidate = row[2]
    
    #have all the votes stored in vote list
    #now just need to go through candidate list
    #and add 1 for each candidate when their name shows up in votes list

print(len(votes_list))
print(candidate_list)