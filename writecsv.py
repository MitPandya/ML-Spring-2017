import csv
import os
import MDP_process2
import subprocess
import sys

#from subprocess import call


pos=13
while(pos != 5):
	included_cols = [0, 1, 2, 3, 4, 5]
	x = pos
	for i in range(0, 8):
		included_cols.append(x)
		x += 1
	while(included_cols[13] != 129):
		with open('MDP_Original_data2.csv', 'r') as csv_file:
			reader = csv.reader(csv_file, delimiter = ',')
			with open('Testing_data.csv', 'w') as newcsv:
				writer = csv.writer(newcsv, delimiter=',')	
				for row in reader:
					colmn = list(row[i]for i in included_cols)
					zip(*colmn)
					#print(colmn)
					writer.writerow(colmn)
			newcsv.close()
			MDP_process2.induce_policy_MDP('Testing_data.csv')
			#subprocess.call([sys.executable, 'MDP_process2.py', '-input', 'Testing_data.csv'])
			#subprocess.Popen("MDP_process2.py -input Testing_data.csv", shell=True)
			#os.system("MDP_process2.py -input Testing_data.csv")
			file = open('textfile.txt', 'a')
			for i, val in enumerate(included_cols):
				file.write(str(included_cols[i]) + ' ')
			file.write('\n')
			file.close()
			for k in range(pos, 14):
				included_cols[k] += 1
				#print(included_cols[i])
		#os.remove('Testing_data.csv')
	csv_file.close()
	file = open('textfile.txt', 'r')
	file.close()
	max = 0
	pos -= 1
'''for line in file:
	if (max < int(line)):
		max = int(line)
		string = file.read

print (max)
print (string)'''


