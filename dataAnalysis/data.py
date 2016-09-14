import csv
f = open('Data.csv')
csv_f = csv.reader(f, delimiter=',')
corn = []
winter_wheat = []
spring_wheat = []
soyabean = []
states  = []
for row in csv_f:
	states.append(row[1]) 
unique_states = set(states)
states = list(unique_states)
print states

acres_planted = 0

for st in unique_states:
	for row in csv_f:
		if row[1] == st:
			print "state: %s" %st