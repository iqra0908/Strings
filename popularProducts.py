
processedData = []

def ties(myDict):
	maxVal = max(myDict.values())
	res = []
	for x in myDict:
		if maxVal == myDict[x]:
			res.append(x)
	return res
	
def rankByProduct(data):
	myDict = dict()
	seenUsers = set()
	for x in data:
		if x[0]+x[1] not in seenUsers:
			if x[1] in myDict:
				myDict[x[1]] += 1
			else:
				myDict[x[1]] = 1
		seenUsers.add(x[0]+x[1])
	
	print(ties(myDict))
	
def rankByQuantity(data):
	myDict = dict()
	for x in data:
		if x[1] in myDict:
			myDict[x[1]] += x[2]
		else:
			myDict[x[1]] = x[2]
	print(ties(myDict))
	

def processJSON(lines):
	global processedData
	for x in lines:
		l = [i for i in x.replace('"','').replace('{','').replace('}','').split(",") if i.strip()]
		linesList = []
		for j in range(len(l)):
			value = [i for i in l[j].split(":") if i.strip()][1].strip()
			if j == 2:
				value = float(value)
			linesList.append(value)
		processedData.append(linesList)

with open('D:/python/SWE sample data - Q2 data.tsv') as f:
	lines = f.read().splitlines()
'''p = {"user_id" : "uid_1", "product_id" : "pid_1", "quantity" : 45}
{"user_id" : "uid_1", "product_id" : "pid_2", "quantity" : 1}
{"user_id" : "uid_2", "product_id" : "pid_2", "quantity" : 5}'''
#lines = p.splitlines()
processJSON(lines)
#print(processedData)
rankByProduct(processedData)
rankByQuantity(processedData)