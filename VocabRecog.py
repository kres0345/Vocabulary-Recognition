#!/usr/bin/python3
from re import sub
from os import listdir
from os.path import join

comparisonFolderPath = 'Comparison data'
inputFileName = 'input.txt'


inputData = sub("[^a-zA-Z ]+", "", open(inputFileName,'r').read().replace("\n"," "))
inputData = inputData.split(" ")
global ComparisonData, CompFileNamesGlob, CompNegScores;
ComparisonData = []
CompFileNamesGlob = []
CompNegScores = []

def LoadComparisonData():
    global ComparisonData, CompFileNamesGlob;
    i=0;CompFilenames=listdir(comparisonFolderPath)
    while(i<len(CompFilenames)):
        ComparisonData.append(sub("[^a-zA-Z ]+", "", open(join(comparisonFolderPath,CompFilenames[i]),'r').read().replace("\n"," ")))
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

    #Insert complex cool code here :D
'''
def percent(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    try:
        result = (num1 / num2 * 100) #num1 / num2 * 100
    except ZeroDivisionError:
        result = 100
    percentage = '{0:.2f}'.format(result)
    return percentage'''

def percent(a, b):
    try:
        return round(a / b * 100, 2)
    except ZeroDivisionError:
        return round(100, 2)

CompareData()
print('''
---------------------------
--- Input file: {0}
--- Comparison files: {1}
---------------------------
'''.format(inputFileName, str(CompFileNamesGlob)))
i=0
while(i<len(CompFileNamesGlob)):
    print("-{0} unlikelihood: {1}, Words not in vocab: {2} / {3}".format(CompFileNamesGlob[i], str(percent(CompNegScores[i],len(inputData)))+'%',CompNegScores[i], len(inputData)))
    i+=1
#print(CompFileNamesGlob)
#print(CompNegScores)