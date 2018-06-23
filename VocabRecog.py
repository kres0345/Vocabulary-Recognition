#!/usr/bin/python3
from re import sub
from os import listdir
from os.path import join

comparisonFolderPath = 'Comparison data'
inputFileName = 'input.txt'

global ComparisonData, CompFileNamesGlob;
ComparisonData = []
CompFileNamesGlob = []

def LoadComparisonData():
    global ComparisonData, CompFileNamesGlob;
    i=0;CompFilenames=listdir(comparisonFolderPath)
    while(i<len(CompFilenames)):
        ComparisonData.append(sub("[^a-zA-Z ]+", "", open(join(comparisonFolderPath,CompFilenames[i]),'r').read().replace("\n"," ")))
        CompFileNamesGlob.append(CompFilenames[i])
        i+=1

def CompareData():
    LoadComparisonData()
    #Insert complex cool code here :D



CompareData()