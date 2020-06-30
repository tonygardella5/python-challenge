import os
import csv
total_votes = 0
first_votes=0
second_votes=0 
third_votes=0
fourth_votes= 0
#county = []
candidate = []
file = 'Resources/PyPoll_Resources_election_data.csv'
file_out = 'analysis/analysis.txt'

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)    
    for row in csvreader:
        total_votes = total_votes + 1        
        #county.append(row[1])
        candidate.append(row[2])
    #print(total_votes)
    #print(county)
    #print(candidate)
    unique_list = list(set(candidate))
    
    #print(unique_list)     
    for i in range(len(candidate)):
        if candidate[i] == unique_list[0]:
            first_votes = first_votes + 1
        elif candidate[i] == unique_list[1]:
            second_votes = second_votes +1
        elif candidate[i] == unique_list[2]:
            third_votes = third_votes + 1 
        elif candidate[i] == unique_list[3]:
            fourth_votes = fourth_votes + 1
        else:
            print("Candidate not found")
    #print(li_votes, khan_votes, correy_votes, tool_votes )
    all_vote_dict = {unique_list[0]:first_votes, unique_list[1]:second_votes, unique_list[2]:third_votes, unique_list[3]:fourth_votes}
    #print(all_vote_dict)
    max_votes = max(all_vote_dict, key=all_vote_dict.get)
    #print(max_votes)
    first_perc ="{:.3%}".format(first_votes/total_votes)
    second_perc = "{:.3%}".format(second_votes/total_votes)
    third_perc = "{:.3%}".format(third_votes/total_votes)
    fourth_perc = "{:.3%}".format(fourth_votes/total_votes)
print("Election Results\n")
print("----------------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("----------------------------------\n")
print(f"{unique_list[0]}: {first_perc} ({first_votes})\n")
print(f"{unique_list[1]}: {second_perc} ({second_votes})\n")
print(f"{unique_list[2]}: {third_perc} ({third_votes})\n")
print(f"{unique_list[3]}: {fourth_perc} ({fourth_votes})\n")
print("----------------------------------\n")
print(f"Winner: {max_votes}\n")
print("----------------------------------\n")

file_write = open(file_out, 'w')       
file_write.write("Election Results\n")
file_write.write("----------------------------------\n")
file_write.write(f"Total Votes: {total_votes}\n")
file_write.write("----------------------------------\n")
file_write.write(f"{unique_list[0]}: {first_perc} ({first_votes})\n")
file_write.write(f"{unique_list[1]}: {second_perc} ({second_votes})\n")
file_write.write(f"{unique_list[2]}: {third_perc} ({third_votes})\n")
file_write.write(f"{unique_list[3]}: {fourth_perc} ({fourth_votes})\n")
file_write.write("----------------------------------\n")
file_write.write(f"Winner: {max_votes}\n")
file_write.write("----------------------------------\n")
file_write.close()