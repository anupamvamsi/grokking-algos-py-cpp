import random

array = []
for i in range(0, 10):
    array.append(random.randint(-200, 200))

print("\nUnsorted array:", array)


def insertionSort(array):
    if array == []:
        return "[]"

    smallest = array[0]
    num = len(array)
    idx = -1

    while num > 0:

        for i in range(idx, len(array)):
            if smallest > array[i]:
                smallest = array[i]

        array.remove(smallest)
        array.insert(idx, smallest)

        idx += 1
        smallest = array[idx]

        num -= 1

    return array


print("\nSorted array:", insertionSort(array))
