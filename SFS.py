from sklearn.neighbors import KNeighborsClassifier
from pandas import read_csv
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
import sys

# The name of the algorithm should be given as input
if len(sys.argv) != 2:
    print('SFS.py < SFS SBS SFFS SBFS >')
    sys.exit(1)

function = sys.argv[1]
# check if input is correct
if function not in ['SFS', 'SBS', 'SFFS', 'SBFS']:
	print('SFS.py < SFS SBS SFFS SBFS >')
	sys.exit(1)

url = "MDP_Original_data2.csv"
names = ['student', 'currProb', 'course', 'session', 'priorTutorAction', 'reward', 'Interaction', 'hintCount', 'TotalTime', 'TotalPSTime', 'TotalWETime', 'avgstepTime', 'avgstepTimePS', 'stepTimeDeviation', 'symbolicRepresentationCount', 'englishSymbolicSwitchCount', 'Level', 'probDiff', 'difficultProblemCountSolved', 'difficultProblemCountWE', 'easyProblemCountSolved', 'easyProblemCountWE', 'probAlternate', 'easyProbAlternate', 'RuleTypesCount', 'UseCount', 'PrepCount', 'MorphCount', 'OptionalCount', 'NewLevel', 'SolvedPSInLevel', 'SeenWEinLevel', 'probIndexinLevel', 'probIndexPSinLevel', 'InterfaceErrorCount', 'RightApp', 'WrongApp', 'WrongSemanticsApp', 'WrongSyntaxApp', 'PrightAppRatio', 'RrightAppRatio', 'F1Score', 'FDActionCount', 'BDActionCount', 'DirectProofActionCount', 'InDirectProofActionCount', 'actionCount', 'UseWindowInfo', 'NonPSelements', 'AppCount', 'AppRatio', 'hintRatio', 'BlankRatio', 'HoverHintCount', 'SystemInfoHintCount', 'NextStepClickCountWE', 'PreviousStepClickCountWE', 'deletedApp', 'ruleScoreMP', 'ruleScoreDS', 'ruleScoreSIMP', 'ruleScoreMT', 'ruleScoreADD', 'ruleScoreCONJ', 'ruleScoreHS', 'ruleScoreCD', 'ruleScoreDN', 'ruleScoreDEM', 'ruleScoreIMPL', 'ruleScoreCONTRA', 'ruleScoreEQUIV', 'ruleScoreCOM', 'ruleScoreASSOC', 'ruleScoreDIST', 'ruleScoreABS', 'ruleScoreEXP', 'ruleScoreTAUT', 'cumul_Interaction', 'cumul_hintCount', 'cumul_TotalTime', 'cumul_TotalPSTime', 'cumul_TotalWETime', 'cumul_avgstepTime', 'cumul_avgstepTimeWE', 'cumul_avgstepTimePS', 'cumul_symbolicRepresentationCount', 'cumul_englishSymbolicSwitchCount', 'cumul_difficultProblemCountSolved', 'cumul_difficultProblemCountWE', 'cumul_easyProblemCountSolved', 'cumul_easyProblemCountWE', 'cumul_probAlternate', 'cumul_easyProbAlternate', 'cumul_RuleTypesCount', 'cumul_UseCount', 'cumul_PrepCount', 'cumul_MorphCount', 'cumul_OptionalCount', 'cumul_probIndexinLevel', 'cumul_InterfaceErrorCount', 'cumul_RightApp', 'cumul_WrongApp', 'cumul_WrongSemanticsApp', 'cumul_WrongSyntaxApp', 'cumul_PrightAppRatio', 'cumul_RrightAppRatio', 'cumul_F1Score', 'cumul_FDActionCount', 'cumul_BDActionCount', 'cumul_DirectProofActionCount', 'cumul_InDirectProofActionCount', 'cumul_actionCount', 'cumul_UseWindowInfo', 'cumul_NonPSelements', 'cumul_AppCount', 'cumul_AppRatio', 'cumul_hintRatio', 'cumul_BlankRatio', 'cumul_HoverHintCount', 'cumul_SystemInfoHintCount', 'cumul_NextStepClickCountWE', 'cumul_PreviousStepClickCountWE', 'cumul_deletedApp', 'CurrPro_NumProbRule', 'CurrPro_avgProbTime', 'CurrPro_avgProbTimePS', 'CurrPro_avgProbTimeDeviationPS', 'CurrPro_avgProbTimeWE', 'CurrPro_avgProbTimeDeviationWE', 'CurrPro_medianProbTime']
dataframe = read_csv(url, names=names, dtype=object)
array = dataframe.values
X = array[1:,6:130]
y = array[1:,5]
ylist = y.flatten()
yfinal = y.ravel()

knn = KNeighborsClassifier(n_neighbors=4)

# Sequential Forward Selection
def callSFS():
	sfs1 = SFS(knn, 
	           k_features=8, 
	           forward=True, 
	           floating=False, 
	           verbose=2,
	           scoring='accuracy',
	           cv=0)

	sfs1 = sfs1.fit(X, yfinal)
	print sfs1.subsets_

# Sequential Backward Selection
def callSBS():
	sbs = SFS(knn, 
	          k_features=8, 
	          forward=False, 
	          floating=False, 
	          scoring='accuracy',
	          cv=4,
	          n_jobs=-1)

	sbs = sbs.fit(X, yfinal)
	print sbs.subsets_

'''print('\nSequential Backward Selection (k=3):')
print(sbs.k_feature_idx_)
print('CV Score:')
print(sbs.k_score_)'''

# Sequential Floating Forward Selection
def callSFFS():
	sffs = SFS(knn, 
	           k_features=8, 
	           forward=True, 
	           floating=True, 
	           scoring='accuracy',
	           cv=4,
	           n_jobs=-1)

	sffs = sffs.fit(X, yfinal)
	print sffs.subsets_

# Sequential Floating Backward Selection
def callSFBS():
	sfbs = SFS(knn, 
	           k_features=8, 
	           forward=False, 
	           floating=True, 
	           scoring='accuracy',
	           cv=4,
	           n_jobs=-1)
	
	sfbs = sfbs.fit(X, yfinal)
	print sfbs.subsets_

if function == 'SFS':
	callSFS()
elif function =='SBS':
	callSBS()
elif function == 'SFFS':
	callSFFS()
elif function == 'SBFS':
	callSBFS()