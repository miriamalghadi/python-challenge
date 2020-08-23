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
   
    with open(electioncsv,'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None)

        for row in csvReader: 
            TotalCount = TotalCount + 1
            Candidate.append(row[2])
        for x in set(Candidate):
            CandidateUnique.append(x)
            cc = Candidate.count(x)
            CVoteCount.append(cc)
            CVotePercent.append(Candidate.count(x)/TotalCount)
        
        Winner = CandidateUnique[CVoteCount.index(max(CVoteCount))]
