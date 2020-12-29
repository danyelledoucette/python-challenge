import os
import csv

budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

months = 0
profits = []
dates = []

with open(budget_data_csv, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        months += 1
        dates.append(row[0])
        profits.append(float(row[1]))
        
total_profit = profits[0]
total_changes = 0
lrg_inc = 0
lrg_dec = 0
        
for n in range (1, months):
    
    total_profit += profits[n]
    current = profits[n] - profits[n-1]
    total_changes += current
    
    if current > lrg_inc:
                lrg_inc = current
                lrg_inc_date = dates[n]
    elif current < lrg_dec:
                lrg_dec = current
                lrg_dec_date = dates[n]
                
    print(f"Financial Analysis")
    print(f"-------------------")
    print(f"Total Months: {months}")
    print(f"Total Profits: ${(total_profit):.2f} ")
    print(f"Average Change: ${(total_changes/(months -1)):.2f}" )
    print(f"Greatest Increase in Profits: {lrg_inc_date} (${(lrg_inc):.2f}) " )
    print(f"Greatest Decrease in Profits: {lrg_dec_date} (${(lrg_dec):.2f}) " )
    
    with open("Financial_Analysis.txt","w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f"Months: {Months}\n")
        txtfile.write(f"Total Profits: ${(TotalProfits):.2f}\n")
        txtfile.write(f"Average Change: ${(TotaledChanges/(Months - 1)):.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {BigIncDate} (${(BigInc):.2f})\n")
        txtfile.write(f"Greatest Decrease in Profits: {BigDecDate} (${(BigDec):.2f})\n")