import os, os.path
import csv

list = os.listdir("./raw_data")
number_files = len(list)

for numbers in range(number_files):
    electioncsv = os.path.join('raw_data',"election_data_" + str(numbers+1) + ".csv")
    
    County= []
    Candidate = []
    CandidateUnique =[]
    CVoteCount = []
    CVotePercent =[]
    TotalCount = 0