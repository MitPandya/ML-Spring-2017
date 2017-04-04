import csv
import os
import MDP_process2
import subprocess
import sys

#from subprocess import call
included_cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



while(included_cols[6] != 122):
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
	csv_file.close()
	if (included_cols[6] != 122):
		if (included_cols[7] != 123):
			if(included_cols[8] != 124):
				if(included_cols[9] != 125):
					if(included_cols[10] != 126):
						if(included_cols[11] 1= 127):
							if(included_cols[12] != 128):
								if(included_cols[13] != 129):
									included_cols[13] += 1
								else:
									included_cols[12] +=1
									included_cols[13] = included_cols[12] + 1
							else:
								included_cols[11] += 1
								included_cols[12] = included_cols[11] + 1
								included_cols[13] = included_cols[12] + 1
						else:
							included_cols[10] +=1 
							included_cols[11] = included_cols[10] + 1
							included_cols[12] = included_cols[11] + 1
							included_cols[13] = included_cols[12] + 1
					else:
						included_cols[9] +=1
						included_cols[10] = included_cols[9] + 1 
						included_cols[11] = included_cols[10] + 1
						included_cols[12] = included_cols[11] + 1
						included_cols[13] = included_cols[12] + 1
				else:
					included_cols[8] += 1
					included_cols[9] = included_cols[8]+1
					included_cols[10] = included_cols[9] + 1 
					included_cols[11] = included_cols[10] + 1
					included_cols[12] = included_cols[11] + 1
					included_cols[13] = included_cols[12] + 1
			else:
				included_cols[7] += 1
				included_cols[8] = included_cols[7] + 1
				included_cols[9] = included_cols[8] + 1
				included_cols[10] = included_cols[9] + 1 
				included_cols[11] = included_cols[10] + 1
				included_cols[12] = included_cols[11] + 1
				included_cols[13] = included_cols[12] + 1
		else:
			included_cols[6] += 1
			included_cols[7] = included_cols[6] + 1
			included_cols[8] = included_cols[7] + 1
			included_cols[9] = included_cols[8] + 1
			included_cols[10] = included_cols[9] + 1 
			included_cols[11] = included_cols[10] + 1
			included_cols[12] = included_cols[11] + 1
			included_cols[13] = included_cols[12] + 1
'''for line in file:
	if (max < int(line)):
		max = int(line)
		string = file.read

print (max)
print (string)'''


