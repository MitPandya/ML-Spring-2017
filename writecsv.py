import csv
import MDP_process2

with open('MDP_Original_data2.csv', 'r') as csv_file:

	reader = csv.reader(csv_file, delimiter = ',')
	included_cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	while(included_cols[13] != 129):
		with open('Testing_data.csv', 'w') as newcsv:
			writer = csv.writer(newcsv, delimiter=',')
			for row in reader:
				colmn = list(row[i]for i in included_cols)
				zip(*colmn)
				writer.writerow(colmn)
		MDP_process2.induce_policy_MDP()
		file = open('textfile.txt', 'a')
		for i, val in enumerate(included_cols):
			if (i>5):
				file.write(str(included_cols[i]) + ' ')
		file.write('\n')
		file.close()
		for i, val in enumerate(included_cols):
			if (i>5):
				included_cols[i] += 1
	file = open('textfile.txt', 'r')
	max = 0
	for line in file:
		if (max < int(line)):
			print(file.read)
			break
		file.read

