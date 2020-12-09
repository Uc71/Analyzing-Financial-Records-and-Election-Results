import csv
import os
import sys
PyBankStuff = os.path.join('Resources', 'PyBankData.csv')
with open(PyBankStuff, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    profit=[]
    next(csvreader)
    first_row=next(csvreader)
    months=1
    changemax=0
    changemin=0
    datemax=""
    datemin=""
    totalprof=int(first_row[1])
    firstprofit=int(first_row[1])
    for row in csvreader:
        totalprof=totalprof+int(row[1])
        months=months+1
        change=(int(row[1])-int(firstprofit))
        profit.append(change)
        if change>changemax:
            changemax=change
            datemax=row[0]
        if change<changemin:
            changemin=change
            datemin=row[0]
        firstprofit=int(row[1])
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(months))
    print("Total Profit: "+str(totalprof))
    print("Average Change: $"+str(round((sum(profit)/(months-1)),2)))
    print("Greatest Increase in Profits: "+str(datemax)+" ($"+str(max(profit))+")")
    print("Greatest Decrease in Profits: "+str(datemin)+" ($"+str(min(profit))+")")
    with open ("PyBankanalysis.txt", "w") as f:
        print("Financial Analysis", file=f)
        print("----------------------------", file=f)
        print("Total Months: "+str(months), file=f)
        print("Total Profit: "+str(totalprof), file=f)
        print("Average Change: $"+str(round((sum(profit)/(months-1)),2)), file=f)
        print("Greatest Increase in Profits: "+str(datemax)+" ($"+str(max(profit))+")", file=f)
        print("Greatest Decrease in Profits: "+str(datemin)+" ($"+str(min(profit))+")", file=f)