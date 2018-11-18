def binarySearch(values, k):
	top = len(values)-1
	bottom = 0
	values.sort()
	print(values)
	found = False
	while(found != True):
		mid = (top+bottom) // 2
		if(values[mid] == k):
			print(str(k) + " found at index: " + str(top))
			found = True
			return True
		elif(values[mid] < k):
			bottom = mid + 1 
		elif(values[mid] > k):
			top = mid - 1
		else:
			return "Not found"


values = [1,2,3,4,5,6,7]
binarySearch(values, 3)