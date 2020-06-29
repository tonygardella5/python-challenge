import os
import csv

file = 'C:/Users/tonyg/Desktop/Bootcamp/python-challenge/PyBank/Resources/PyBank_Resources_budget_data.csv'
total_month = 0
total_amount = 0
total_change = 0
values = []
change_list = []
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    
    for row in csvreader:        
        values.append(int(row[1]))
        total_month = total_month + 1
        total_amount = total_amount + int(row[1])
    #before = values[0]
    #after = int(row[1]) 
    #print(values[1]-values[0])  
    for i in range(len(values)):
        if i > 0:
            change_list.append(values[i]-values[i-1])
    for i in range(len(change_list)):
        total_change = total_change + change_list[i]
    max(change_list)

    #changes = (after - before) / len(change_list)
    changes = round(total_change / len(change_list), 2)



    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: {total_amount}")
    print(f"Average Change: ${changes}")
    print(f"Greatest Increase in Profits: (${max(change_list)})")
    print(f"Decrease in Profits: (${min(change_list)})")