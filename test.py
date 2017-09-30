def checkExist(date, corpName) :
    for row in dic[date] :
        if row[0] == corpName :
            return True
    return False


stocks = [['1995', 'corp A', 10.12, 23.12, 94], ['1996', 'corp A', 20.34, 23.12, 94.22], 
['1997', 'corp A', 30.32, 23.12, 94], ['1994', 'corp B', 22.22, 23.12, 94.22], 
['1995', 'corp B', 27.13, 23.12, 94], ['1996', 'corp B', 14.43, 23.12, 94.22], 
['1996', 'corp C', 20.76, 23.12, 94], ['1997', 'corp C', 30.54, 23.12, 94.22], 
['1998', 'corp C', 22.66, 23.12, 94]]

dic = {}


for list in stocks :
    if list[0] in dic :
        if checkExist(list[0], list[1]) :
            break
    	dic[list[0]].append(list[1:])
    else :
        dic[list[0]] = []
    	dic[list[0]].append(list[1:])

for list in dic :
    print(list)
    for record in dic[list] :
        print('{:10}'.format(record[0]) + '{:5.2f}'.format(record[1]))


f = open("test.txt", 'w')
for date in dic :
	f.write(date + "\n")
	for item in dic[date] :
	    f.write('{:10}'.format(item[0]) + '{:8.2f}'.format(item[1]))
        f.write('{:8.2f}'.format(item[2]) + '(' +'{:5}'.format(item[3]) + ')' )
f.write("\n")
f.close()

