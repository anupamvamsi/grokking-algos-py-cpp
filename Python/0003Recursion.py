# A Python code to execute different functions implemented using Recursion.

# array = 3 5 9 22 13 14    : Sample Input
# print(array.pop(0))       : Returns the value removed from the list/array. 

# Hanoi Problem (Referenced and written from the Computerphile YouTube video on Recursion.)
# Link to the video: https://www.youtube.com/watch?v=8lhxIOAfDss
def move(f, t):
    print("Moving from {} to {}.".format(f, t))
            
# move("A", "B")
def moveVia(f, v, t):
    move(f, v)
    move(v, t)

def hanoi(n, f, h, t):
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, h) # Moving n-1 disks from to via by using target as an auxiliary position.
        move(f, t)
        hanoi(n-1, h, f, t) # Moving n-1 disks from helper position to the target using from position as an auxiliary position.


# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Fibonacci
def fibonacci(n):
    if n <= 0:
        return "Incorrect Input! Should've entered a number greater than zero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Summming an array:
def sumAnArray(array):
    
    if len(array) == 0:
        return 0
    else:
        return array.pop(0) + sumAnArray(array) # pop(index) returns element removed and modifies array


# Count items in an array:
def countItemsInArray(array):

    if len(array) == 0:
        return 0
    else:
        return int(0 if array.remove(array[0]) is None else 0) + 1 + countItemsInArray(array) # remove(e) returns 'None' where 'e' is element


# Find Max number in an array:
def findMaxInArray(array, n):
    if n == 1:
        return array[0]
    else:
        return (array[n-1] if array[n-1] >= findMaxInArray(array, n-1) else findMaxInArray(array, n-1))


# Find Min number in an array:
def findMinInArray(array, n):
    if n == 1:
        return array[0]
    else:
        return min(array[n-1], findMinInArray(array, n-1))


if __name__ == "__main__":
    global n
    global array

    hano = "hanoiexe"
    fact = "factorialexe"
    fibo = "fibonacciexe"
    suma = "sumAnArrayexe"
    coun = "countItemsInArrayexe"
    maxi = "findMaxInArrayexe"
    mini = "findMinInArrayexe"

    inp = input("Enter 'hano' | 'fact' | 'fibo' | 'suma' | 'coun' | 'maxi' | 'mini' for Hanoi, Factorial, Fibonacci, Sum of an Array, Count items in an Array, Find Max in an Array and Find Min in an Array, respectively:\n")
    print("\n")


    def hanoiexe(n):
        return hanoi(n, "A", "B", "C")


    def factorialexe(n):
        print(f'Factorial of {n} is {factorial(n)}!\n')

    
    def fibonacciexe(n):
        print(f'The Fibonacci series for {n} numbers is: ')
        for i in range(1, n+1):
            print(fibonacci(i), end=" ")
        print("\n")


    def sumAnArrayexe(array):
        print(f'Sum of {array} is: {sumAnArray(array)}!\n')


    def countItemsInArrayexe(array):
        print(f'Number of items in {array} is {countItemsInArray(array)}!\n')


    def findMaxInArrayexe(array, n):
        print(f'Maximum element in {array} is {findMaxInArray(array, n)}!\n')


    def findMinInArrayexe(array, n):
        print(f'Minimum element in {array} is {findMinInArray(array, n)}!\n')


    fname = globals()[inp]      # Convert string to function call1
    func = globals()[fname]     # Convert string to function call2
    
    if inp == 'hano' or inp == 'fact' or inp == 'fibo':
        n = int(input("Enter n: "))
        print("\n")
        func(n)

    if inp == 'suma' or inp == 'coun' or inp == 'maxi' or inp == 'mini':
        array = list(map(int, input("Enter array: ").split()))
        print("\n")

        n = len(array)
        if inp == 'maxi' or inp == 'mini':
            func(array, n)
        else:
            func(array)

# execDic = {
#         'hano': "hanoiexe",
#         'fact': "factorialexe",
#         'fibo': "fibonacciexe",
#         'suma': "sumAnArrayexe",
#         'coun': "countItemsInArrayexe",
#         'maxi': "findMaxInArrayexe",
#         'mini': "findMinInArrayexe"
#     }