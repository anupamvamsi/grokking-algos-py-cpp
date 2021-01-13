'''
Creating a multiplication table with all the elements in the array. So
if your array is [2, 3, 7, 8, 10], you first multiply every element by 2,
then multiply every element by 3, then by 7, and so on.
'''


def mulArr(array):
    
    if len(array) < 2:
        return array
    else:
        arr1 = []
        for i in range(0, len(array)):
            pivot = array[i]
            arr1 = [(pivot * item) for item in (array[0:i] + array[i+1:])]
            arr1.insert(i, pivot * pivot)
            print(pivot, arr1)


def RecMulArr(array, n):    # Recursive Function
    
    if n == len(array):
        return "\nDone multiplying!"
    else:
        arr1 = list(array)  # Why is list(array) is used? Whenever you try to copy one array's contents into another's, only the REFERENCE OF THE ARRAY is copied. Not the contents.
        pivot = arr1.pop(n)
        if pivot >= 0: # Just for beautification of the Output
            print(f'Multiplying with +{pivot}    : {[(pivot * item) for item in (array[:])]}')
        else:
            print(f'Multiplying with {pivot}    : {[(pivot * item) for item in (array[:])]}')
        return RecMulArr(array, n+1)


# To generate sample input arrays
import random

array = []
for i in range(6): # number of numbers
    array.append(random.randint(-9, 9)) # start and end limits

# array = [2, 4, 1, -3, -7, 0]
print(f'\nOriginal Array         : {array}')
print("\n", end="")
print(RecMulArr(array, 0))
print("\n", end="")
# print(mulArr(array))

# def MulArr(array):     # Non-recursive, only FIRST element is used to multiply
    
#     if len(array) < 2:
#         return array
#     else:
#         arr1 = list(array)
#         # print(arr1)
#         pivot = arr1.pop(0)
#         # print(pivot, arr1)
#         return [(pivot * item) for item in (array[:])]

# TESTS
# array = [30, 592, -9, 22, -13, 142]
# pivot = array[2] * array[2] 
# array = [(array[2] * item) for item in (array[0:2] + array[2+1:])]
# array.insert(2, pivot)
# print(array)