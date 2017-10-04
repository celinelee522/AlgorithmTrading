#import numpy as np
import pandas as pd
from math import log10


# time consuming
def checkExist(date, corpName) :
    for list in dateDic[date] :
        if list[0] == corpName :
            return True
    return False

def findDate(date, corpName) : # should return log(mark cap)
    date = int(date)

    count = 0
    while count < 3 :
        for list in companies[corpName] :
            if (date == int(list[0])) :
                print("List of targeted date : %s" %list)
                return list[1]
        count += 1
        date += 1


def computeGrowth(base, yearsLater):
    if yearsLater != None :
        return (yearsLater/base - 1) * 100.0
    else :
        return 0


in_file = open('seryung1.txt', 'r')

#finance_dict = {"date":{}, "corpName":{}, "cshoc":{}, "prccd" :{}}


id = 0

labels = []

firstLine = in_file.readline()
firstLine = firstLine.strip()
firstLine = firstLine.split()

labels.append(firstLine[2])
labels.append(firstLine[3])
labels.append(firstLine[4])
labels.append(firstLine[5])

#print(labels)

companies = {} #dictionary

for row in in_file:
    row = row.strip()
    row = row.split("\t")
    row = row[2:6]

    stock = [] 

    if (len(row) == 4) and (row[0] != 'datadate') and (row[2] != '') and (row[3] != '') : # for irregular data
        stock.append(row[0]) # date
        date = row[0]
        #stock.append(row[1])  # company name
        company = row[1]
        row[2] = int(float(row[2])) # share of outstanding
        row[3] = int(float(row[3])) # share price
        if (row[2]*row[3] > 0):
            mktCap = round( log10(row[2]*row[3]), 2 )
            stock.append(mktCap) # ln(market capitalization)
            # stock = [Date, Corp name, ln(market cap)]
            #company = stock[1]

            if company in companies : # date already exists as a key
                companies[company].append(stock)
            else : # date doesn't exist so you have to add one
                companies[company] = []
                companies[company].append(stock)
# finished making up dictionary(key == company name). 
# values inside key are bunch of lists [date, log(market Cap)]


f = open("newStockList.txt", 'w')
for company in companies : 
    if company == 'DAEWOO ENGINEERING CONSTRUC' :
        f.write('DAEWOO ENGINEERING CONSTRUC\n')
        for row in companies[company] :
            list = [None] * 9
            list[0] = row[0] # date
            list[1] = row[1] # market capitalization
            oneYearLater = int(list[0]) + 10000
            twoYearLater = int(list[0]) + 20000
            threeYearLater = int(list[0]) + 30000

            mktCap_one = findDate(oneYearLater, company)
            list[2] = mktCap_one
            list[3] = computeGrowth(list[1], mktCap_one) # growth rate a year after
            grthRate_one = int(computeGrowth(list[1], mktCap_one))

            mktCap_two = findDate(twoYearLater, company)
            list[4] = mktCap_two
            list[5] = computeGrowth(list[1], mktCap_two) # growth rate two years after
            grthRate_two = int(computeGrowth(list[1], mktCap_two))

            mktCap_three = findDate(twoYearLater, company)
            list[6] = mktCap_three
            list[7] = computeGrowth(list[1], mktCap_three) # growth rate three years after
            grthRate_three = int(computeGrowth(list[1], mktCap_three))
            print("<base year: %s> 1 year later market cap : %s( %f)/ 2 years later market cap : %s( %f)/ 3 years later market cap : %s( %f)" %(list[0], mktCap_one, grthRate_one, mktCap_two, grthRate_two, mktCap_three, grthRate_three))

            sorted(companies.keys())
            
            f.write('{:10}'.format(list[0]) + '{:10.2f}'.format(list[1])) #date, marketCapitalization
            #if (list[2] is not None and list[3] is not None and list[4] is not None and list[5] is not None and list[6] is not None and list[7] is not None) :
            for i in range(1,4) :
                i = 2*i
                print("i : %d" %i)
                if (list[i] is not None) :
                    f.write('{:7.2f}'.format(float(list[i])) + '(' + '{:3.1f}'.format(list[i+1]) + ')')
                else :
                    f.write('  None(None)')
            f.write('\n')

f.close()




in_file.close()




