#need to fix o_votes.  1 too manyd
import os
import csv

import operator
from decimal import Decimal

csvpath = os.path.join("election_data.csv")
output_path = os.path.join("election.txt")

total_votes = 0
k_votes =0
c_votes = 0
l_votes =0
o_votes =0
missed_votes =0
count = 0
temp = 0

with open(csvpath, 'r') as csvfile:
    #print(text)
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = True
    for record in csvreader:
              
        if len(record)>1:
            curr_county =record[1]
            curr_name = record[2]
            curr_votes = record[0]

            #skips and saves header
            if header == True:
                header = record   
                
            elif curr_name =="Khan":
                k_votes = k_votes+1
                total_votes +=1
                curr_name = "clear"

            elif curr_name =="Correy":
                c_votes = c_votes+1
                total_votes +=1
                curr_name = "clear"

            elif curr_name =="Li":
                l_votes = l_votes+1
                total_votes +=1
                curr_name = "clear"

            elif curr_name =="O'Tooley":
                o_votes +=1
                total_votes +=1
                curr_name = "clear"

            else:
                missed_votes += 1
    
        else:
            print(f"this is an extra line with: '{s_row[0]}''")

k_percentage = round(Decimal(k_votes/(total_votes)*100),3)
c_percentage = round(Decimal(c_votes/(total_votes)*100),3)
l_percentage = round(Decimal(l_votes/(total_votes)*100),3)
o_percentage = round(Decimal(o_votes/(total_votes)*100),3)

#calculating winner
stats = {"Khan":k_percentage,"Corry":c_percentage,"Li":l_percentage,"O'Tooley":o_percentage}
winner =(max(stats.items(), key =operator.itemgetter(1))[0])

print(f"Total Votes: {total_votes}") 
print(f"Khan has a total of {k_votes} votes and {k_percentage}%")
print(f"Corry has a total of {c_votes} votes and {c_percentage}%")
print(f"Li has a total of {l_votes} votes and {l_percentage}%")
print(f"O'Tooley has a total of {o_votes} votes and {o_percentage}%")
print("-------------------------------")
print(f"The winner is {winner}")

file1 = open(output_path,"w") 
L = ["Election Results \n",
     "----------------------------\n",
     f"Total Votes: {total_votes} \n",
     "----------------------------\n",
     f"Khan: {k_percentage}% ({k_votes}) \n",
     f"Correy: {c_percentage}% ({c_votes}) \n",
     f"Li: {l_percentage}% ({l_votes}) \n",
     f"O'Tooley: {o_percentage}% ({o_votes})\n",
     "----------------------------\n",
     f"Winner: {winner}\n",
     "----------------------------\n"]  
 
file1.write("Daniel Bradley \n") 
file1.writelines(L) 
file1.close()  