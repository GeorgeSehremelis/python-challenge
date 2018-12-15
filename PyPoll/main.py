import os
import csv

pypoll_csv = "election_data.csv"
count = 0
candidates = []
vote_count = {}
Khan=0
Correy=0
Li=0
Tooley = 0


with open(pypoll_csv, newline="") as pypollcsv:
	csvreader = csv.reader(pypollcsv, delimiter = ",")
	head = next(csvreader)

	for row in csvreader: 
		count += 1

		if row[2] not in candidates:
			candidates.append(row[2])
			print(candidates)

		if row[2] == candidates[0]: 
			Khan += 1
		elif row[2] == candidates[1]:
			Correy +=1
		elif row[2] == candidates[2]:
			Li +=1
		elif row[2] == candidates[3]:
			Tooley +=1
		else: 
			print("nothing")

print(Khan/count)
print(Correy/count)
print(Li/count)
print(Tooley/count)		

print(f'{candidates[0]}: {100*Khan/count}% ({Khan})')
print(f'{candidates[1]}: {100*Correy/count}% ({Correy})')
print(f'{candidates[2]}: {100*Li/count}% ({Li})')
print(f'{candidates[3]}: {100*Tooley/count}% ({Tooley})')

		


#Total Votes: 3521001
#['Khan', 'Correy', 'Li', "O'Tooley"]
# Khan: 63.00001050837532% (2218231)
#Correy: 19.999994319797125% (704200)
#Li: 13.999996023857989.3f% (492940)
#O'Tooley: 2.999999147969569% (105630)

#Winner: Khan

