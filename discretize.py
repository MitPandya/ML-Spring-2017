from __future__ import division
from pandas import read_csv
import pandas as pd
import numpy as np
import csv
from scipy.stats import binned_statistic
import os

url = "MDP_Original_data2.csv";
names = ['student', 'currProb', 'course', 'session', 'priorTutorAction', 'reward', 'Interaction', 'hintCount', 'TotalTime', 'TotalPSTime', 'TotalWETime', 'avgstepTime', 'avgstepTimePS', 'stepTimeDeviation', 'symbolicRepresentationCount', 'englishSymbolicSwitchCount', 'Level', 'probDiff', 'difficultProblemCountSolved', 'difficultProblemCountWE', 'easyProblemCountSolved', 'easyProblemCountWE', 'probAlternate', 'easyProbAlternate', 'RuleTypesCount', 'UseCount', 'PrepCount', 'MorphCount', 'OptionalCount', 'NewLevel', 'SolvedPSInLevel', 'SeenWEinLevel', 'probIndexinLevel', 'probIndexPSinLevel', 'InterfaceErrorCount', 'RightApp', 'WrongApp', 'WrongSemanticsApp', 'WrongSyntaxApp', 'PrightAppRatio', 'RrightAppRatio', 'F1Score', 'FDActionCount', 'BDActionCount', 'DirectProofActionCount', 'InDirectProofActionCount', 'actionCount', 'UseWindowInfo', 'NonPSelements', 'AppCount', 'AppRatio', 'hintRatio', 'BlankRatio', 'HoverHintCount', 'SystemInfoHintCount', 'NextStepClickCountWE', 'PreviousStepClickCountWE', 'deletedApp', 'ruleScoreMP', 'ruleScoreDS', 'ruleScoreSIMP', 'ruleScoreMT', 'ruleScoreADD', 'ruleScoreCONJ', 'ruleScoreHS', 'ruleScoreCD', 'ruleScoreDN', 'ruleScoreDEM', 'ruleScoreIMPL', 'ruleScoreCONTRA', 'ruleScoreEQUIV', 'ruleScoreCOM', 'ruleScoreASSOC', 'ruleScoreDIST', 'ruleScoreABS', 'ruleScoreEXP', 'ruleScoreTAUT', 'cumul_Interaction', 'cumul_hintCount', 'cumul_TotalTime', 'cumul_TotalPSTime', 'cumul_TotalWETime', 'cumul_avgstepTime', 'cumul_avgstepTimeWE', 'cumul_avgstepTimePS', 'cumul_symbolicRepresentationCount', 'cumul_englishSymbolicSwitchCount', 'cumul_difficultProblemCountSolved', 'cumul_difficultProblemCountWE', 'cumul_easyProblemCountSolved', 'cumul_easyProblemCountWE', 'cumul_probAlternate', 'cumul_easyProbAlternate', 'cumul_RuleTypesCount', 'cumul_UseCount', 'cumul_PrepCount', 'cumul_MorphCount', 'cumul_OptionalCount', 'cumul_probIndexinLevel', 'cumul_InterfaceErrorCount', 'cumul_RightApp', 'cumul_WrongApp', 'cumul_WrongSemanticsApp', 'cumul_WrongSyntaxApp', 'cumul_PrightAppRatio', 'cumul_RrightAppRatio', 'cumul_F1Score', 'cumul_FDActionCount', 'cumul_BDActionCount', 'cumul_DirectProofActionCount', 'cumul_InDirectProofActionCount', 'cumul_actionCount', 'cumul_UseWindowInfo', 'cumul_NonPSelements', 'cumul_AppCount', 'cumul_AppRatio', 'cumul_hintRatio', 'cumul_BlankRatio', 'cumul_HoverHintCount', 'cumul_SystemInfoHintCount', 'cumul_NextStepClickCountWE', 'cumul_PreviousStepClickCountWE', 'cumul_deletedApp', 'CurrPro_NumProbRule', 'CurrPro_avgProbTime', 'CurrPro_avgProbTimePS', 'CurrPro_avgProbTimeDeviationPS', 'CurrPro_avgProbTimeWE', 'CurrPro_avgProbTimeDeviationWE', 'CurrPro_medianProbTime']
#names = ['student', 'currProb', 'course', 'session', 'priorTutorAction', 'reward', 'Interaction', 'hintCount']
dataframe = read_csv(url, names=names, dtype = object)
array = dataframe.values

X = array[1:,]

def discretize_and_write(col):

	Xfinal =  X[0:,col].astype(np.float)

	max_value = max(Xfinal)
	min_value = min(Xfinal)
	avg_value = sum(Xfinal)/len(Xfinal)

	a = sorted(Xfinal)

	l = len(a)

	b1 = a[int(l/4)]
	b2 = a[int(l/2)]
	b3 = a[int(3*l/4)]

	bin_list = [-np.inf,b1,b2,b3,max_value]
	bin_list = sorted(list(set(bin_list)))
	print bin_list
	label = []
	for i in range(len(bin_list)-1):
		label.append(i)

	factor = pd.cut(Xfinal,bin_list, labels=label)
	arr = factor[0:,]
	b = map(lambda x: x, arr)
	print(pd.value_counts(factor))
	return b

def histogram_disc(col):
	Xfinal =  X[0:,col].astype(np.float)

	hist,bin_list = np.histogram(Xfinal, bins=4)
	label = []
	for i in range(len(bin_list)):
		label.append(i)

	list_bins = list(bin_list)
	list_bins.insert(0,-np.inf)

	factor = pd.cut(Xfinal,list_bins, labels=label)
	arr = factor[0:,]
	b = map(lambda x: x, arr)
	print(pd.value_counts(factor))
	return b


selected_features = [119, 120, 57, 74, 123, 12, 106, 30]
discretized_features = []

for i in selected_features:
	discretized_features.append(discretize_and_write(i))

features = []
features.append(('student','currProb','course','session','priorTutorAction','reward','feature1','feature2','feature3','feature4','feature5','feature6','feature7','feature8'))
#features.append(('feature1','feature2','feature3','feature4','feature5','feature6','feature7','feature8'))
#119, 120, 57, 74, 123, 12, 106, 30

existing_features = []
with open('sample_output.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        existing_features.append(row)
csv_file.close()

for j in range(len(discretized_features[0])):
		features.append((list(existing_features[j+1])+list((discretized_features[0][j],discretized_features[1][j],discretized_features[2][j],discretized_features[3][j],discretized_features[4][j],discretized_features[5][j],discretized_features[6][j],discretized_features[7][j]))))
		#features.append(((discretized_features[0][j],discretized_features[1][j],discretized_features[2][j],discretized_features[3][j],discretized_features[4][j],discretized_features[5][j],discretized_features[6][j],discretized_features[7][j])))

with open('discretized_output.csv','w') as out:
	writer = csv.writer(out, delimiter = ',')
	for row in features:
		writer.writerow(row)
out.close()

os.system("python MDP_process2.py -input discretized_output.csv")

'''with open('a.csv', 'wb') as out:
    writer = csv.writer(out)
    writer.writerows(discretized_features)
out.close()

included_cols = []
for i in range(7168):
	included_cols.append(i)

with open('a.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    with open('SFS.csv', 'w') as newcsv:
        writer = csv.writer(newcsv, delimiter = ',')
        for row in reader:
            zip(*row)
            writer.writerow(row)
    newcsv.close()
csv_file.close()'''