import os
import csv

pybank_csv = "budget_data.csv"
count = 0
profits = 0
last = 867884
change_list = []
maxi = 0
mini = 0

with open(pybank_csv, newline="") as budgetcsv:
	csvreader = csv.reader(budgetcsv, delimiter = ",")
	head = next(csvreader)

	for row in csvreader:
		count += 1

		x = int(row[1])
		profits += x
		change = x - last
		change_list.append(change)
		if change > maxi:
			maxi = change
			max_date = row[0]
		elif change < mini:
			mini = change
			min_date = row[0]



		last = int(row[1])

average_change = (sum(change_list)/count)

print(mini)
print(min_date)
# max_increase = max(change_list)
# max_decrease = min(change_list)


#86 is the answer
# profits = 38382578
# average change in profits = -2288.19
#1926159 , Feb-2012
#-2196167 , Sep-2013


		