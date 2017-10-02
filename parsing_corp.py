#import numpy as np
import pandas as pd
from math import log10


# time consuming
def checkExist(date, corpName) :
    for list in dateDic[date] :
        if list[0] == corpName :
            return True
    return False

def findDate(date, corpName, count) : # should return log(mark cap)
    date = int(date)
    for list in companies[corpName] :
        if (date == list[0]) :
            print("List of targeted date : %s" %list)
            return list[1]
    date += 1
    count += 1
    if (count < 5) :
        print("recursive call")
        findDate(date, corpName, count)
    print("not found...")

def computeGrowth(base, yearsLater):
    if yearsLater != None :
        return (yearsLater/base - 1) * 100
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

companies = {}

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
            marketCap = round( log10(row[2]*row[3]), 2 )
            stock.append(marketCap) # ln(market capitalization)
            # stock = [Date, Corp name, ln(market cap)]
            #company = stock[1]

            if company in companies : # date already exists as a key
                companies[company].append(stock)
            else : # date doesn't exist so you have to add one
                companies[company] = []
                companies[company].append(stock)
# finished making up dictionary(key == company name). 
# values inside key are bunch of lists [date, log(market Cap)]

for company in companies : 
    for list in companies[company] :
        print(list)
        date = list[0]
        marketCap = list[1]
        oneYearLater = int(date) + 10000
        twoYearLater = int(date) + 20000
        threeYearLater = int(date) + 30000

        oneYMarCap = findDate(oneYearLater, company, 0)
        list.append(oneYMarCap)
        list.append(int(computeGrowth(marketCap, oneYMarCap)))
        print("one year later : %s, market cap : %s " %(oneYearLater, oneYMarCap))

        twoYMarCap = findDate(twoYearLater, company, 0)
        list.append(twoYMarCap)
        list.append(int(computeGrowth(marketCap, twoYearLater)))
        print("two year later : %s, market cap : %s " %(twoYearLater, twoYMarCap))

        threeYMarCap = findDate(twoYearLater, company, 0)
        list.append(threeYMarCap)
        list.append(int(computeGrowth(marketCap, threeYMarCap)))
        print("three year later : %s, market cap : %s " %(threeYearLater, threeYMarCap))


"""

sorted(dateDic.keys())
f = open("newStockList.txt", 'w')
for date in dateDic:
	f.write(date + "\n")
	for item in dateDic[date] :
	    f.write('{:30}'.format(item[0]) + '{:10.2f}'.format(item[1]) + "\n") #compName, marketCapitalization
        f.write('{:7.2f}'.format(float(item[2])) + '(' + '{:2}'.format(item[3]) + ')') # oneYearAfter, growthRate
        f.write('{:7.2f}'.formate(float(item[4])) + '(' + '{:2}'.format(item[5]) + ')')
        f.write('{:7.2f}'.formate(float(item[7])) + '(' + '{:2}'.format(item[8]) + ')' + "\n")
f.close()

"""



in_file.close()




