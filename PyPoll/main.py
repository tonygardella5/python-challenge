import os
import csv
total_votes = 0
max_candidate = 0
votes_list = []
votes_perc = []
candidate = []
file = 'Resources/PyPoll_Resources_election_data.csv'
file_out = 'analysis/analysis.txt'

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)    #read in
    
    for row in csvreader:
        total_votes = total_votes + 1        #create total
        candidate.append(row[2]) #create lists

    unique_list = list(set(candidate)) # creates unique list of candidates
    votes_list = [0] * len(unique_list) #creates vote count list the same size as unique candidate list
         
    for i in range(len(candidate)):     #creates vote count list with same index as candidate list
        for j in range(len(unique_list)):
            if candidate[i] == unique_list[j]:
                votes_list[j] = votes_list[j] + 1

    max_votes = max(votes_list) #determines max votes
    
    for i in range(len(votes_list)):
        if votes_list[i] == max_votes:
            max_candidate = i           #finds i in max votes list to apply to unique candidate list
     
    for i in range(len(votes_list)):
        votes_perc.append("{:.3%}".format(votes_list[i]/total_votes)) #turns all total votes into percentages

print("Election Results\n")
print("----------------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("----------------------------------\n")
for i in range(len(votes_list)):
    print(f"{unique_list[i]}: {votes_perc[i]} ({votes_list[i]})\n") #loop for each name
print("----------------------------------\n")
print(f"Winner: {unique_list[max_candidate]}\n")
print("----------------------------------\n")

file_write = open(file_out, 'w')       
file_write.write("Election Results\n")
file_write.write("----------------------------------\n")
file_write.write(f"Total Votes: {total_votes}\n")
file_write.write("----------------------------------\n")
for i in range(len(votes_list)):
    file_write.write(f"{unique_list[i]}: {votes_perc[i]} ({votes_list[i]})\n") ##loop for each name
file_write.write("----------------------------------\n")
file_write.write(f"Winner: {unique_list[max_candidate]}\n")
file_write.write("----------------------------------\n")

file_write.close()