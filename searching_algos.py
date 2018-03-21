""" Search algorithms in Python.
"""

# Linear Search: This algo can work with both SORTED and UNSORTED array too.

# 1. Start from the leftmost element of arr[] and one by one compare x with each element of arr[].
# 2. If x matches with an element, return the index.
# 3. If x doesn't match with any of elements, return -1.
# Time Complexity: O(n)

def linear_search(arr, x):
	for index in range(len(arr)):
		if arr[index] == x:
			return index+1

	return -1

arr = [2, 3, 4, 1, 9, 7]
x = 9
print linear_search(arr, x)


# Binary Search: This algo only works with SORTED array.

# 1. Compare x with the middle element.
# 2. If x matches with middle element, we return the mid index.
# 3. Else If x is greater than the mid element, then x can only lie in right half subarray after
#  the mid element. So we recur for right half.
# 4. Else (x is smaller) recur for the left half.

# Time Complexity: O(log n)

# Recursive implementation of Binary Search:
def binary_search_recursive(arr, start_index, end_index, key):
	# Base case.
	if end_index>=start_index:
		mid = start_index + (end_index-start_index)/2
		# When key is middle element.
		if arr[mid] == key:
			return mid+1
		elif arr[mid]>key: # When key is smaller than mid element.
			return binary_search_recursive(arr, start_index, mid-1, key)
		else: # When key is bigger than mid element.
			return binary_search_recursive(arr, mid+1, end_index, key)
	else:
		return -1

arr = range(1, 10, 1)
key = 9

res = binary_search_recursive(arr, 0, len(arr)-1, key)

if res !=-1:
	print "Key {} found at {}".format(key, res)
else:
	print "Key not found in given array!"

# Iterative implementation of Binary Search:
def binary_search_iterative(arr, start_index, end_index, key):
	while end_index>=start_index:
		mid = start_index + (end_index-start_index)/2

		# When key is middle element.
		if arr[mid] == key:
			return mid+1
		elif arr[mid]>key: # When key is smaller than mid element.
			end_index = mid - 1
		else: # When key is bigger than mid element.
			start_index = mid + 1

	return -1

arr = range(1, 10, 1)
key = 5

res = binary_search_iterative(arr, 0, len(arr)-1, key)

if res !=-1:
	print "Key {} found at {}".format(key, res)
else:
	print "Key not found in given array!"
	