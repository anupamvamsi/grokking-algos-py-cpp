'''
Excerpts from the book "Grokking Algorithms" by Aditya Bhargava:
D&C algorithms are RECURSIVE algorithms.
    To solve a problem using D&C, there are two steps:
        1. Figure out the base case. This should be the simplest possible case.
        2. Divide or decrease your problem until it becomes the base case.

Euclid’s algorithm:
    “If you find the biggest box that will work for this size, that will be the
    biggest box that will work for the entire farm.”

Explanation of the algorithm: 
    https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
'''
# Sample input  : 3 5 9 13 14 22


def dividePlot(length, breadth):
    if breadth == 0:
        return length
    else:
        return dividePlot(breadth, (length % breadth))


def binSearchDnC(low, high, array, item):
    mid = int((low + high) / 2)
    guess = array[mid]

    if high >= low:
        if  guess == item:
            return mid
        elif guess < item:
            return binSearchDnC(mid + 1, high, array, item)
        elif guess > item:
            return binSearchDnC(low, mid - 1, array, item)
    else:
        return None


def quickSort(array):
    if len(array) < 2: # Empty array or array with only one element 
        return array
    else:
        pivot = array[0]
        lesser = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quickSort(lesser) + [pivot] + quickSort(greater)


if __name__ == "__main__":

    divi = "dividePlotexe"
    bins = "binSearchDnCexe"

    inp = input("Enter:\n'divi' if you want to divide a plot\n'bins' if you want to search for an item in an array:\n")
    print("\n")


    def dividePlotexe(l, b):
        print(f'The plot of {l} x {b} can be divided into is a square with side = {dividePlot(l, b)}')

    
    def binSearchDnCexe(low, high, array, item):
        if binSearchDnC(low, high, array, item) == None:
            print(f"{item} not found in array {array}!")
        else:
            print(f'{item} is located at index {binSearchDnC(low, high, array, item)} in {array}.')


    fname = globals()[inp]      # Convert string to function call1
    func = globals()[fname]     # Convert string to function call2
    
    if inp == 'divi':
        l = int(input('Enter length (> breadth) of plot: '))
        b = int(input('Enter breadth (< length) of plot: '))
        print("\n")

        func(l, b)
    
    if inp == 'bins':
        array = list(map(int, input("Enter array: ").split()))
        if array == []:
            print("Empty array! Aborting.")
        else:
            array = quickSort(array)
            print(f"Array has been modified to: {array}")
            item = int(input("Enter number you want to search for: "))
            func(0, len(array) - 1, array, item)
