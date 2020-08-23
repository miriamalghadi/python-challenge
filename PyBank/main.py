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

    avrevchg = totalrevchange / itemcount
    g_increase = max(revenuechange)
    g_decrease = min(revenuechange)
    increasedate = date[revenuechange.index(g_increase)]
    decreasedate = date[revenuechange.index(g_decrease)]
    count_m = len(set(date))

    with open('financial_analysis_report_' + str(numbers + 1) + '.txt, "w') as text:
        text.write("Financial Analysis for file 'budget_data_"+ str(numbers+1) + ".csv'"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("    Total Months: " + str(CountM) + "\n")
        text.write("    Total Revenue: " + "$" + str(TotalRev) +"\n")
        text.write("    Average Revenue Change: " + '$' + str(int(AveRevChg)) +'\n')
        text.write("    Greatest Increase in Revenue: " + str(IncreaseDate) + " ($" + str(GIncrease) + ")\n")
        text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate) + " ($" + str(GDecrease) + ")\n\n")
        #finally