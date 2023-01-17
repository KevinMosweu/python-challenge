#Import necessary modules
import os
import csv

#List to store dates
date_list=[]

#List to store monthly changes in profits/losses
changes_list=[]

#Set initial value for previous month proft/loss
lastmonth = 0

#Set initial value for total
total = 0

#Specify path for CSV file to be read
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#Open and read the CSV
with open(budget_data_csv, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Store header
    csv_header = next(csvfile)
    
    #Loop through rows collect date,
    #Add monthly profit/loss to total,
    #Calculate change in profit/loss from previous month and store it
    for row in csvreader:
        date_list.append(row[0])
        total = total + int(row[1])
        change = int(row[1]) - lastmonth
        lastmonth = int(row[1])
        changes_list.append(change)
    
    #Find greatest increase/decrease in monthly changes, find corresponding date in date list
    greatest_increase = [date_list[changes_list.index(max(changes_list))], max(changes_list)]
    greatest_decrease = [date_list[changes_list.index(min(changes_list))], min(changes_list)]
    
    #Remove first value of changes as technicaly there is no change for the first month
    #Proceed to calculate average, rounded to two decimal places
    changes_list.pop(0)
    average_change = round(sum(changes_list)/len(changes_list), 2)
    
    #Print heading and calculates values to terminal
    print("Financial Analysis")
    print('')
    print('-------------------------------')
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

#Specify path to write text file to
fin_analysis_txt= os.path.join('Analysis', 'Financial_Analysis.txt')

#Write heading and calculated values to text file
with open(fin_analysis_txt, 'w') as textfile:
    textfile.write('Financial Analysis\n')
    textfile.write('\n')
    textfile.write('-------------------------------\n')
    textfile.write('\n')
    textfile.write(F'Total Months: {len(date_list)}\n')
    textfile.write('\n')
    textfile.write(f'Total: ${total}\n')
    textfile.write('\n')
    textfile.write(f'Average Change: ${average_change}\n')
    textfile.write('\n')
    textfile.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
    textfile.write('\n')
    textfile.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
    textfile.close