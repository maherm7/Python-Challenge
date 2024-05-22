import os
import csv

#Setting the path to the Data file
results = os.path.join("PyBank", "analysis", "results.txt")
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

#Declaring the variables 
total_months = 0
net_total = 0
monthly_changes = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

#Opening the file as a read file
with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    previous_profit_loss = 0

#Looping to get the total months and net total
    for row in csv_reader:
        total_months += 1
        net_total += int(row[1])

#Calculating the monthly change
        if previous_profit_loss != 0:
            monthly_change = int(row[1]) - previous_profit_loss
            monthly_changes.append(monthly_change)

#Calculating the greatest increase
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_date = row[0]

#Calculating the greatest decrease
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_date = row[0]

        previous_profit_loss = int(row[1])

avg_change = sum(monthly_changes) / len(monthly_changes)

#Printing the results
print("Financial Analysis")
print("---------------------------------")
print("Total Months:", total_months)
print("Total: $", net_total)
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write the results to a text file
with open("results.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${avg_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
