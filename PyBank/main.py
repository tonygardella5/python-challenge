import os
import csv

file = 'Resources/PyBank_Resources_budget_data.csv'
file_out = 'analysis/analysis.txt'
total_month = 0
total_amount = 0
total_change = 0
lookup_value_max = 0
lookup_value_min = 0
values = []
dates = []
change_list = []
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)    
    for row in csvreader:        
        values.append(int(row[1]))
        dates.append(row[0])
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

    #changes = (after - before) / len(change_list)
    changes = round(total_change / len(change_list), 2)

    max_change = max(change_list)
    min_change = min(change_list)

    for i in range(len(change_list)):
        if change_list[i] == max_change:
            lookup_value_max = i
    for i in range(len(change_list)):
        if change_list[i] == min_change:
            lookup_value_min = i
    #print(len(change_list))
    #print(len(dates))
    max_date = dates[lookup_value_max + 1]
    #print(max_date)
    min_date = dates[lookup_value_min + 1]
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: {total_amount}")
    print(f"Average Change: ${changes}")
    print(f"Greatest Increase in Profits: {max_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_change})")

    #print(dates)
file_write = open(file_out, 'w')       
file_write.write("Financial Analysis\n")
file_write.write("----------------------------------\n")
file_write.write(f"Total Months: {total_month}\n")
file_write.write(f"Total: {total_amount}\n")
file_write.write(f"Average Change: ${changes}\n")
file_write.write(f"Greatest Increase in Profits: {max_date} (${max_change})\n")
file_write.write(f"Greatest Decrease in Profits: {min_date} (${min_change})\n")
file_write.close()