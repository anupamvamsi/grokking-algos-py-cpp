myList = [3, 9, 1, -5, 4, 9, -120, 4]

myDict = {
        "Radiohead" : 156,
        "Kishore Kumar" : 141,
        "The Black Keys" : 35,
        "Neutral Milk Hotel" : 94,
        "Beck" : 88,
        "The Strokes" : 61,
        "Wilco" : 111
    } # Dictionary to be sorted

newDict = {} # Dictionary which will have the sorted key and values


# Performing Selection Sort on a Dictionary using Recursion
def selectSortADictionary(myDict):
    intDict = myDict # Internal Dictionary for the function
     
    temp = list(intDict.keys())[0] # Initialising first element of the Dictionary
    
    for item in intDict.keys(): # Finding the smallest value a key has in the Dictionary
        if intDict[temp] >= intDict[item]:
            temp = item
    
    newDict.update({temp: intDict[temp]}) # Updating New Dictionary with the smallest value
    intDict.pop(temp) # Getting rid of the smallest value from the Internal Dictionary

    if not bool(intDict): # Base Case - Checking if the Internal Dictionary is empty or not
        print(newDict) # If empty, prints the New Dictionary which will be the Sorted Result
    else:
        selectSortADictionary(intDict) # Recursive case
    

selectSortADictionary(myDict)


newList = []


# Performing Selection Sort on a Dictionary using Recursion
def selectSortAList(myList):

    intList = myList
    tempListItem = intList[0]
    
    for itemList in intList:
        if tempListItem >= itemList:
            tempListItem = itemList
    
    newList.append(tempListItem)
    intList.remove(tempListItem)

    if not bool(intList):
        print(newList)
    else:
        selectSortAList(intList)


selectSortAList(myList)


def BinarySearch(List, item):
    low = 0
    high = len(List) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = List[mid]

        if item == guess:
            return mid
        elif item > guess:
            low = mid + 1
        elif item < guess:
            high = mid - 1
    return None


print(BinarySearch(newList, 9))
print(BinarySearch(newList, -1))