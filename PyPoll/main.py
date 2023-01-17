#Import necessary modules
import os
import csv

#List to store each vote
votes_list=[]

#List to store each unique candidate
candidate_list = []

#Blank value to compare candidate names against
candidate = ''

#Set path for file to be read
election_data_csv = os.path.join('Resources', 'election_data.csv')

#Opening the CSV
with open(election_data_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Store header row
    csv_header = next(csvfile)
    
    #Loop through rows and store each vote as candidate name in vote_list
    #Also compare if candidate name has been encountered and store in candidate_list if new
    for row in csvreader:
        votes_list.append(row[2])
        if row[2] != candidate and candidate_list.count(row[2])==0:
            candidate_list.append(row[2])
            candidate = row[2]
    
#Printing heading to terminal and also total votes by finding number of votes stored in vote_list    
print("Election Results")
print('')
print('-------------------------')
print('')
print(f'Total Votes: {len(votes_list)}')
print('')
print('-------------------------')

#Loop through list of unique candidates, 
#Count the number of votes, calculate percentage to three decimal places
#Print results to terminal
for candidate in candidate_list:
    votes = votes_list.count(candidate)
    percentage = round((votes/len(votes_list))*100, 3)

    print(f'{candidate}: {percentage}% ({votes})')
    print('')

print('-------------------------')
print('')

#Find winner by finding most frequent name appearing in votes list
mode = max(set(votes_list), key = votes_list.count)

#Print winner to terminal
print(f'Winner: {mode}')

#Set path to write text file to
elec_results_txt= os.path.join('Analysis', 'Election_Analysis.txt')

#Writing previously found results to text file in path above
with open(elec_results_txt, 'w') as textfile:
    textfile.write('Election Results\n')
    textfile.write('\n')
    textfile.write('-------------------------\n')
    textfile.write('\n')
    textfile.write(f'Total Votes: {len(votes_list)}\n')
    textfile.write('\n')
    textfile.write('-------------------------\n')
    textfile.write('\n')

    for candidate in candidate_list:
        votes = votes_list.count(candidate)
        percentage = round((votes/len(votes_list))*100, 3)

        textfile.write(f'{candidate}: {percentage}% ({votes})\n')
        textfile.write('\n')
    
    textfile.write('-------------------------\n')
    textfile.write('\n')
    textfile.write(f'Winner: {mode}')
    textfile.close