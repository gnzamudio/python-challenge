import os
import csv

filepath= os.path.join("Resources\budget_data.csv")

with open(filepath,'r') as csvfile:
    csvreader= csv.reader(csvfile,delimiter= ',')
    next (csvreader,None)

#create an empty list to collect all months in that list and create a variable to keep track of the change in profit

    date= []
    changeinmoney= 0

#variables to keep track of the changes and the month when it happened
    changes=[]
    greatest=0
    least=0
    dategreat=''
    dateleast= ''
    before=0
    output=[]

    for row in csvreader:
        months =row[0]
        netprofit= int(row[1])
        date.append(months)
        changeinmoney += int(netprofit)
        change=netprofit-before
        changes.append(change)

        if change> greatest:
            greatest=change
            dategreat= months
        elif change< least:
            least= change
            dateleast= months
    before= netprofit

changes.pop(0)
finalchange= 0
for eachmonth in changes:
    finalchange += eachmonth

#print summary of analysis, use append to alter use when creating the file
print("Analysis\n----------")
output.append("Analysis\n----------")

print(f"Total months: {len(date)}")
output.append(f"\nTotal Months: {len(date)}")

print(f"Total: ${changeinmoney}")
output.append(f"\nTotal: ${changeinmoney}")

#calculate average change, round to 2 decimal places
print(f"Average change: ${round(finalchange/len(changes),2)}")
output.append(f"\nAverage Change: ${round(finalchange/len(changes),2)}")

print(f"Greatest Profit Increase: {dategreat} (${greatest})")
output.append(f"\nGreatest Profit Increase: {dategreat} (${greatest})")

print(f"Greatest Profit Decrease: {dateleast} (${least})")
output.append(f"\nGreatest Profit Decrease: {dateleast} (${least})")

textfile= open("Analysis.txt",'w')
print(textfile)