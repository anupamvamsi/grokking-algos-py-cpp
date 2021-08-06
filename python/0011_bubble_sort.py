import random

array = []
for i in range(10):
    array.append(random.randint(-200, 200))

print("\nUnsorted array:", array, "\n")


def bubbleSort(array):
    length = len(array)

    if length == 0:
        return "[]"

    for iteration in range(0, length):
        swap = False
        for i in range(0, length - 1 - iteration):  # not comparing last element(s)
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swap = True
        if swap == False:
            print("Breaking early as no swap has occurred.")
            break

        print(f"Iteration number {iteration+1}: {array}")

    return array


print("\nSorted array:", bubbleSort(array))
