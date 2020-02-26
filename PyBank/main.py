import csv
import os

csvpath = os.path.join("budget_data.csv")
output_path = os.path.join("budget.txt")

total = 0
count = 0
temp = 0
greatest_increase =0
greatest_decrease =0
great_month="xxx-0000"
bad_month="xxx-0000"
month_date = "xxx-0000"

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = True
    first_value = True

    for record in csvreader:
        #skips over empty line
        if len(record)>1:
            curr_date = record[0]
            curr_profit = record[1]
        
        #This is counting duplicate months.  Finding no duplicates the #months = #records
        if month_date == curr_date:
            print("Duplicate")
        else:
            month_date = curr_date

        #header is assigned True and the renamed to save header and skip when calculating    
        if header == True:
            header = record

        #first_value is assigned True to skip 2nd line when calculating difference between months       
        elif first_value == True:
            first_month = curr_profit
            first_value = False
            count = count +1 
            
        else:
            count = count +1
            ave_change=round((int(curr_profit)-int(first_month))/(count-1),2)
            profit_round = int(curr_profit)-int(temp)
            
            if profit_round > greatest_increase:
                greatest_increase=profit_round
                great_month = curr_date
                
            elif profit_round < greatest_decrease:
                greatest_decrease=profit_round
                bad_month = curr_date        
       
        if curr_profit != "Profit/Losses":
            total = total+int(curr_profit)

        temp = curr_profit

#results printed out to terminal      
print(f"Total Months: {count}")
print(f"Total: {total}")
print(f"Average Change: {ave_change}")
print(f"Greatest Increase is {great_month} in am amount of ${greatest_increase}")
print(f"Greatest Increase is {bad_month} in am amount of ${greatest_decrease}")

#results Exported to text file
file1 = open(output_path,"w") 
L = ["Financial Analysis \n",
"----------------------------\n",
f"Total Months: {count} \n",
f"Total: {total} \n",
f"Average Change: ${ave_change} \n",
f"Greatest Increase in Profits: {great_month} (${greatest_increase}) \n",
f"Greatest Decrease in Profits: {bad_month} (${greatest_decrease})"
]  
 
file1.write("Daniel Bradley \n") 
file1.writelines(L) 
file1.close()