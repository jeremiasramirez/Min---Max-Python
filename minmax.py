
def minval(arr):
	i = 0
	j = 0
	changeval = 0
	minval = 0
	while i < len(arr):
		while j < len(arr):
			if arr[j] >= arr[i]:
				minval = arr[j]
				return minval
			else:
				changeval = arr[i]
				return changeval
			j+=1
		i+=1

def maxval(arr):
	i = 0
	j = 0
	changeval = 0
	maxval = 0
	while i <= len(arr):
		while j < len(arr):
			if arr[j] > arr[i]:
				changeval = arr[j]

			else:
				maxval = arr[i]
			j+=1
		i+=1
	return changeval


 
