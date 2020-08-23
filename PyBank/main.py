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
            itemcount - itemcount + 1
            date.append(row[0])
            revenue.append(int(row[1]))
            totalrev = totalrev + int(row[1])
            revend = int(row[1])
            revchg = revend - revbeg
            totalrevchange totalrevchange + revchg
            revenuechange.append(revchg)
            splitdate = row[0].split('-')
            month.append(str(splitdate[0]))
            year.append(splitdate[1][-2:])
            revbeg = revend

            