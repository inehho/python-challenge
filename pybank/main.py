import os
import csv 

bankpath = os.path.join("..", "Pybank", "budget_data.csv")

monthtotal = []
netprofit = []
change_inprofit = []

with open(bankpath, newline='') as bankfile:   
    csvreader = csv.reader(bankfile, delimiter=',')
    header = next(csvreader)

 #this to get the count of rows
    #totalcount = (sum(1 for row in csvreader)) 
    #print(totalcount)
    

    for row in csvreader:
        monthtotal.append(row[0])
        netprofit.append(int(row[1]))
        #diff = 0

    for i in range(len(netprofit)-1):
        change_inprofit.append(netprofit[i+1]-netprofit[i+1])

max_value = max(change_inprofit)
max_decrease = min(change_inprofit)
max_month_increase = change_inprofit.index(max(change_inprofit))
max_month_decrease = change_inprofit.index(min(change_inprofit))

print("  Financial Analysis  ")
print("-------------------------")
print(f"Total Month: {len(monthtotal)}")
print(f"Total: ${sum(netprofit)}")
print(f"Average Change: {round(sum(change_inprofit)/len(change_inprofit))}")
print(f"Greatest Increase in Profits: {monthtotal[max_month_increase]}")
print(f"Greatest Decrease in Profits: {monthtotal[max_month_decrease]}")

#create a zipped list
clean_bankdata = zip(monthtotal,netprofit,change_inprofit)

#Setting output file path
myoutput = os.path.join("new_budgetdata.csv")

#open the output file
with open(myoutput, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Total_Per_Month,Netprofit,Change_inProfit"])

    writer.writerow(clean_bankdata)