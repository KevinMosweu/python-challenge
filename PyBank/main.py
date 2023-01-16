import os
import csv

date_list=[]

changes_list=[]

lastmonth = 0

total = 0

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_data_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
        date_list.append(row[0])
        total = total + int(row[1])
        change = int(row[1]) - lastmonth
        lastmonth = int(row[1])
        changes_list.append(change)
    
    changes_list.pop(0)
    average_change = round(sum(changes_list)/len(changes_list), 2)

    print(len(date_list))
    print(total)
    print(average_change)
