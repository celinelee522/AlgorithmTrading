#import numpy as np
import pandas as pd
from math import log10


# time consuming
def checkExist(date, corpName) :
    for list in dateDic[date] :
        if list[0] == corpName :
            return True
    return False

in_file = open('seryung1.txt', 'r')

#finance_dict = {"date":{}, "corpName":{}, "cshoc":{}, "prccd" :{}}


id = 0

stocksList = []
labels = []

firstLine = in_file.readline()
firstLine = firstLine.strip()
firstLine = firstLine.split()

labels.append(firstLine[2])
labels.append(firstLine[3])
labels.append(firstLine[4])
labels.append(firstLine[5])

#print(labels)

dateDic = {}

for row in in_file:
    row = row.strip()
    row = row.split("\t")
    row = row[2:6]

    stock = [] 

    if (len(row) == 0) :
    	pass

    elif (len(row) == 4) and (row[0] != 'datadate') and (row[2] != '') and (row[3] != '') : # for irregular data
        stock.append(row[0]) # date
        date = row[0]
        stock.append(row[1])  # company name
        corpName = row[1]
        row[2] = int(float(row[2])) # share of outstanding
        row[3] = int(float(row[3])) # share price
        if (row[2]*row[3] > 0):
            marketCap = round( log10(row[2]*row[3]), 2 )
            stock.append(marketCap) # ln(market capitalization)
        # stock = [Date, Corp name, ln(market cap)]

            if stock[0] in dateDic : # date already exists as a key
                    dateDic[stock[0]].append(stock[1:])
            else : # date doesn't exist so you have to add one
                dateDic[stock[0]] = []
                dateDic[stock[0]].append(stock[1:])


        """
        date = row[0]
        date = [date]
        date.append(stock)
        dateList.append()

        if date :
            dateList[date] = []
        dateList[date].append(stock[1:])
        """
        #stocksList.append(stock)
# Dictionary data structure for sorting by date
"""      
for list in stock :
    if list[0] in dateDic :
        dateDic[list[0]].append([list[1], list[2]])
    else :
        dateDic[list[0]] = list[1:]
"""

sorted(dateDic.keys())
f = open("newStockList.txt", 'w')
for date in dateDic:
	f.write(date + "\n")
	for item in dateDic[date] :
	    f.write("		%s\n" % item)
	f.write("\n")
f.close()



"""
id = 0
for record in stocksList :
    date = record[id][0] #date information
    
    if (len(row) == 0) :
    	pass
    elif date :
        date.append(record[1:]) #create a list 'date'
    else : 
    	date = []
        date.append(record[1:])    	

    print(date)
"""




#df = pd.DataFrame.from_records(stocksList, columns=labels)



	
#	finance_dict["date"][id] = line[2]
#	finance_dict["corpName"][id] = line[3]
#	finance_dict["cshoc"][id] = line[5]
#	finance_dict["prccd"][id] = line[6]
#	print(finance_dict)
	


in_file.close()

#finance_df = pd.DataFrame({"gvkey": finance_dict["gvkey"], "prccd":finance_dict["prccd"]})
# pd.DataFrame.from_dict()


