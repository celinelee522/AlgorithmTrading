stocks = [['1995', 'corp A', 10], ['1996', 'corp A', 20], 
['1997', 'corp A', 30], ['1994', 'corp B', 22], 
['1995', 'corp B', 27], ['1996', 'corp B', 14], 
['1996', 'corp C', 20], ['1997', 'corp C', 30], 
['1998', 'corp C', 22]]

dic = {}


for list in stocks :
    if list[0] in dic :
    	dic[list[0]].append([list[1], list[2]])
        print('exist')
    else :
    	dic[list[0]] = list[1:]
        print('create')

print(dic)

f = open("test.txt", 'w')
for date in dic:
	f.write(date + "\n")
	for item in dic[date] :
	    f.write("		%s\n" % item)
	f.write("\n")
f.close()