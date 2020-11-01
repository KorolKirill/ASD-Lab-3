import time

def insertionSort (table):
	start = time.time()
	
	length = len(table)
	for i in range(1, length):
		key = table[i]
		j = i-1
		while j >=0 and key < table[j]:
			table[j+1] = table[j]
			j -= 1
		table[j+1] = key

	end = time.time()
	estimatedTime = "Insertion sort for "+str(length)+" elements took "+str(end-start)+" seconds"

	return estimatedTime