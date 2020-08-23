import os, os.path
import csv

list = os.listdir("./raw_data")
number_files = len(list)

for numbers in range(number_files):
    budgetcsv = os.path.join('raw_data', "budget_data_" = str(numbers+1) + ".csv")
    date = []
    revenue = []
    month = []
    year = []
    revenuechange = []
    totalrev = 0
    totalrevchange = 0
    revbeg = 0
    itemcount = 0

    with open(budgetcsv, 'r') as csvFile ;
        csvreader = csv.reader(csvfile, delimiter = ',')
        next(csvreader, None)

        for row in csvreader:
            