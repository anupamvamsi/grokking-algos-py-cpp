def quickSort(array):   # Sorting by using the MID element as a pivot (is faster to check)
    if len(array) < 2:  # Empty array or array with only one element 
        return array
    else:
        mid = int((len(array) - 1) / 2)
        pivot = array[mid]
        lesser = [i for i in array[0:mid] + array[mid+1:] if i <= pivot]
        greater = [i for i in array[0:mid] + array[mid+1:] if i > pivot]
        
        return quickSort(lesser) + [pivot] + quickSort(greater)


# To generate sample input arrays
import random

array = []
for i in range(30): # number of numbers
    array.append(random.randint(-8000, 8000)) # start and end limits

print("\n")
print("UNSORTED LIST:")
print(array, len(array))    # Input array
print("\n")

print("SORTED LIST:")
res = quickSort(array)      # Sorted array
print(res, len(res))        # Result O/P
print("\n")


# def quickSort(array):   # Sorting by using the FIRST element as a pivot
#     if len(array) < 2:  # Empty array or array with only one element 
#         return array
#     else:
#         pivot = array[0]
#         lesser = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
        
#         return quickSort(lesser) + [pivot] + quickSort(greater)


# print(quickSort([30, 592, -9, 22, -13, 142]))
# Sample input  : 30 592 -9 22 -13 142

# TESTS
# array = [30, 592, -9, 22, -13, 142]
# mid = int((len(array) - 1) / 2)
# print(array[0:mid] + array[mid+1:])
# print(array[mid:])
# print(array[:mid])