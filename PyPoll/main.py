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
    
print("Election Results")
print('')
print('-------------------------')
print('')
print(f'Total Votes: {len(votes_list)}')
print('')
print('-------------------------')

for candidate in candidate_list:
    votes = votes_list.count(candidate)
    percentage = round((votes/len(votes_list))*100, 3)

    print(f'{candidate}: {percentage}% ({votes})')
    print('')

print('-------------------------')
print('')

mode = max(set(votes_list), key = votes_list.count)


print(f'Winner: {mode}')

elec_results_txt= os.path.join('Analysis', 'Election_Analysis.txt')

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