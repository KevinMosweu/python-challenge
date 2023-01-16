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
    
    greatest_increase = [date_list[changes_list.index(max(changes_list))], max(changes_list)]
    greatest_decrease = [date_list[changes_list.index(min(changes_list))], min(changes_list)]
    changes_list.pop(0)
    average_change = round(sum(changes_list)/len(changes_list), 2)

    print("Financial Analysis")
    print('')
    print('---------------------------------------------')
    print('')
    print(F'Total Months: {len(date_list)}')
    print('')
    print(f'Total: ${total}')
    print('')
    print(f'Average Change: ${average_change}')
    print('')
    print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
    print('')
    print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
