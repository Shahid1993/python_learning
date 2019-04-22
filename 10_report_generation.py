import csv

#Import the data
f_csv = open('winter-is-coming-2018.csv')
headers = next(f_csv)
f_reader = csv.reader(f_csv)
file_data = list(f_reader)

# Make all blank cells into zeroes
# https://stackoverflow.com/questions/2862709/replacing-empty-csv-column-values-with-a-zero

for row in file_data:
	for i, x in enumerate(row):
		if(len(x) < 1):
			x = row[i] = 0
	#print(row)


# Push the data to a dictionary
total_score = {}

# Pass each character and their final score into total_score dictionary
for row in file_data:
	total = (int(row[4]) +
			int(row[5]) +
			int(row[6]) +
			int(row[7]) +
			int(row[8]) +
			int(row[9])
		)

	total_score[row[0]] = total

#print(total_score)

# Dictionaries aren't sortable by default, we'll have to borrow from these two classes.
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
from operator import itemgetter
from collections import OrderedDict

sorted_score = OrderedDict(sorted(total_score.items(), key = itemgetter(1), reverse = True))

#print(sorted_score)

# We get the name of the winner and their score
winner = list(sorted_score)[0]
winner_score = sorted_score[winner]

print(winner + " with " + str(winner_score))
