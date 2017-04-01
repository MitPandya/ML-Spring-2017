# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:16:16 2017

@author: sanan
"""

import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
url = "MDP_Original_data2.csv";
names = ['Reward', 'Interaction', 'hintCount', 'TotalTime', 'TotalPSTime', 'TotalWETime', 'avgstepTime', 'avgstepTimePS', 'stepTimeDeviation', 'symbolicRepresentationCount', 'englishSymbolicSwitchCount', 'Level', 'probDiff', 'difficultProblemCountSolved', 'difficultProblemCountWE', 'easyProblemCountSolved', 'easyProblemCountWE', 'probAlternate', 'easyProbAlternate', 'RuleTypesCount', 'UseCount', 'PrepCount', 'MorphCount', 'OptionalCount', 'NewLevel', 'SolvedPSInLevel', 'SeenWEinLevel', 'probIndexinLevel', 'probIndexPSinLevel', 'InterfaceErrorCount', 'RightApp', 'WrongApp', 'WrongSemanticsApp', 'WrongSyntaxApp', 'PrightAppRatio', 'RrightAppRatio', 'F1Score', 'FDActionCount', 'BDActionCount', 'DirectProofActionCount', 'InDirectProofActionCount', 'actionCount', 'UseWindowInfo', 'NonPSelements', 'AppCount', 'AppRatio', 'hintRatio', 'BlankRatio', 'HoverHintCount', 'SystemInfoHintCount', 'NextStepClickCountWE', 'PreviousStepClickCountWE', 'deletedApp', 'ruleScoreMP', 'ruleScoreDS', 'ruleScoreSIMP', 'ruleScoreMT', 'ruleScoreADD', 'ruleScoreCONJ', 'ruleScoreHS', 'ruleScoreCD', 'ruleScoreDN', 'ruleScoreDEM', 'ruleScoreIMPL', 'ruleScoreCONTRA', 'ruleScoreEQUIV', 'ruleScoreCOM', 'ruleScoreASSOC', 'ruleScoreDIST', 'ruleScoreABS', 'ruleScoreEXP', 'ruleScoreTAUT', 'cumul_Interaction', 'cumul_hintCount', 'cumul_TotalTime', 'cumul_TotalPSTime', 'cumul_TotalWETime', 'cumul_avgstepTime', 'cumul_avgstepTimeWE', 'cumul_avgstepTimePS', 'cumul_symbolicRepresentationCount', 'cumul_englishSymbolicSwitchCount', 'cumul_difficultProblemCountSolved', 'cumul_difficultProblemCountWE', 'cumul_easyProblemCountSolved', 'cumul_easyProblemCountWE', 'cumul_probAlternate', 'cumul_easyProbAlternate', 'cumul_RuleTypesCount', 'cumul_UseCount', 'cumul_PrepCount', 'cumul_MorphCount', 'cumul_OptionalCount', 'cumul_probIndexinLevel', 'cumul_InterfaceErrorCount', 'cumul_RightApp', 'cumul_WrongApp', 'cumul_WrongSemanticsApp', 'cumul_WrongSyntaxApp', 'cumul_PrightAppRatio', 'cumul_RrightAppRatio', 'cumul_F1Score', 'cumul_FDActionCount', 'cumul_BDActionCount', 'cumul_DirectProofActionCount', 'cumul_InDirectProofActionCount', 'cumul_actionCount', 'cumul_UseWindowInfo', 'cumul_NonPSelements', 'cumul_AppCount', 'cumul_AppRatio', 'cumul_hintRatio', 'cumul_BlankRatio', 'cumul_HoverHintCount', 'cumul_SystemInfoHintCount', 'cumul_NextStepClickCountWE', 'cumul_PreviousStepClickCountWE', 'cumul_deletedApp', 'CurrPro_NumProbRule', 'CurrPro_avgProbTime', 'CurrPro_avgProbTimePS', 'CurrPro_avgProbTimeDeviationPS', 'CurrPro_avgProbTimeWE', 'CurrPro_avgProbTimeDeviationWE', 'CurrPro_medianProbTime']
dataframe = pandas.read_csv(url)
array = dataframe.values
X = array[:,0:124]
Y = array[:,0]
# feature extraction
test = SelectKBest(score_func=chi2, k=8)
fit = test.fit(X, Y)
# summarize scores
numpy.set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
# summarize selected features
print(features[0:5,:])

#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']