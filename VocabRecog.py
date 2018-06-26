#!/usr/bin/python3
from re import sub
from os import listdir
from os.path import join

comparisonFolderPath = 'Comparison data'
inputFileName = 'input.txt'


inputData = sub("[^a-zA-Z ]+", "", open(inputFileName,'r').read().lower().replace("\n"," "))
inputData = inputData.split(" ")
global ComparisonData, CompFileNamesGlob, CompNegScores;
ComparisonData = []
CompFileNamesGlob = []
CompNegScores = []

def LoadComparisonData():
    global ComparisonData, CompFileNamesGlob;
    i=0;CompFilenames=listdir(comparisonFolderPath)
    while(i<len(CompFilenames)):
        ComparisonData.append(sub("[^a-zA-Z ]+", "", open(join(comparisonFolderPath,CompFilenames[i]),'r').read().lower().replace("\n"," ")))
        CompFileNamesGlob.append(CompFilenames[i])
        i+=1

def CompareData():
    LoadComparisonData()
    global ComparisonData, CompNegScores, CompFileNamesGlob;
    i=0
    while(i<len(CompFileNamesGlob)):
        CompNegScores.append(0)
        f=0
        while(f<len(inputData)):
            if not(inputData[f] in ComparisonData[i]):
                CompNegScores[i] += 1
            f+=1
        i+=1

def percent(a, b):
    try:
        return round(a / b * 100, 2)
    except ZeroDivisionError:
        return round(100, 2)

CompareData()
print('''
---------------------------
--- Input file: {0}
--- Input string: `{2}`
--- Comparison files: {1}
---------------------------
'''.format(inputFileName, str(CompFileNamesGlob), open(inputFileName, 'r').read().lower().replace("\n"," ")[0:90]))
i=0
while(i<len(CompFileNamesGlob)):
    print("-Unlikelihood: {1}, Words not in vocabulary: {2} / {3}, Filename: {0}".format(CompFileNamesGlob[i], str(percent(CompNegScores[i],len(inputData)))+'%',CompNegScores[i], len(inputData)))
    i+=1
