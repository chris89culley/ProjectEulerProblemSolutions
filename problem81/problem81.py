

def getArrayFromText(text):
	arr = []
	y = -1
	file = open(text, 'r')
	for line in file:
		arr.append([]) 
		y += 1
		data = line.split()
		x = -1
		for t in data: 
			s = t.split(',')
			for d in s:
				arr[y].append([])
				arr[y][x] = int(d)
	return arr

def getMinPath(arr):
	for y in range(0, len(arr)):
		for x in range(0, len(arr[0])):
			if x is 0 and y is 0:
				continue
			if x is 0:
				print "before"
				print arr[y][x]
				print arr[y-1][x]
				arr[y][x] += arr[y-1][x]
				print "after"
				print arr[y][x]
			elif y is 0:
				arr[y][x] += arr[y][x-1]
			else:
				arr[y][x] += min(arr[y-1][x], arr[y][x-1])
				

	print arr[len(arr)-1][len(arr[0])-1]

getMinPath(getArrayFromText("matrix.txt"))




            
