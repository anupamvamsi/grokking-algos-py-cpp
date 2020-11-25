'''
################################################
# REFERENCES
################################################

1. https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/
2. https://codereview.stackexchange.com/questions/69437/make-a-queuet-class-from-scratch-in-python
3. https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly/240205#240205


################################################
# TESTS
################################################

ARR_LENGTH = 4

# INITIATE ARRAY
values = [None] * ARR_LENGTH # Or, instead of " [None] * size " USE, (FOR STORAGE) " [[] for _ in range(size)] "


# TESTING THE INDEX RETRIEVAL WITHIN THE SIZE OF THE ARRAY 'VALUES'
def get_index(key: str):    # Making sure only string input is given to the 'key' argument
    z = hash(key) % len(values)
    return z


print(get_index("bar"))


################################################
# EXAMPLE
################################################

self.array [
    [("foo", 1), ("bar", 2), ],     # Nested array with strings whose hashes evaluate to 0 
    [("hello", 3), ("world", 4)],   # Nested array with strings whose hashes evaluate to 1
]
'''


################################################
# BUILDING THE queueTIONARY
################################################

class HashTable(object):

    # queueTIONARY INITIALIZER
    def __init__(self, length=4):
        self.array = [None] * length    # Vs. " [[] for _ in range(size)] "?
    

    # ADDL. FN. 1
    def __setitem__(self, key, value):
        self.add(key, value)

    
    # ADDL. FN. 2
    def __getitem__(self, key):
        return self.get(key)


    # ADDL. FN. 3
    def __contains__(self, key):
        index = self.hash(key)
        
        if self.array[index] is not None:

            for kvp in self.array[index]:
                if kvp[0] == key:
                    return True
        
        return False

    
    # CHECK IF queueTIONARY IS FULL
    def isqueuetFull(self):
        numItems = 0

        for item in self.array:
            if item is not None:
                numItems += 1
        
        resizeIt = float(numItems / len(self.array))

        # 0.7 is the threshold to decide to double the queuetionary
        return resizeIt >= 0.7 

    
    # RESIZE, RE-ADD ELEMENTS IN queueT IF queueT OCCUPANCY >= 0.7
    def queuetDoubler(self):

        # This step re-initializes the queuetionary to all none values as its elements
        resized_HT = HashTable(length=len(self.array) * 2)

        # Re-adding
        for index in range(len(self.array)):

            # For re-adding
            if self.array[index] is None:
                continue
            
            # Re-adding all values
            for kvp in self.array[index]:
                resized_HT.add(kvp[0], kvp[1])
        
        # Replace original self.array before resizing with resized self.array
        self.array = resized_HT.array

    
    # GET THE INDEX FOR A SPECIFIC STRING IN ARRAY
    def hash(self, key):            
        length = len(self.array)

        # Returns integer within the len of array
        return hash(key) % length   
    
    
    # A KEY: VALUE PAIR IS PASSED TO BE UPDATED, OR ADDED IF MISSING
    def add(self, key, value):

        if self.isqueuetFull():
            self.queuetDoubler()

        index = self.hash(key)

        # If position *index* in self.array is not empty
        if self.array[index] is not None: 

            # Check if the key being called exists in the nested array being accessed
            # If yes, we will have to udpate the [old] key being called. for that:
            for kvp in self.array[index]:

                # Check if key exists among the tuples in the nested array being accessed
                if kvp[0] == key:   
                    key[1] == value # if yes, update the value of the key
                    break           # after updation, come out the for loop

            # If no, we will have to store the [new] key in the nested array being accessed.
            # If the for loop expires without breaking:
            else:   
                self.array[index].append([key, value]) # can be appended as (key, value) as well
        
        # If position *index* is empty in self.array
        else: 
            self.array[index] = []
            self.array[index].append([key, value]) # can use (key, value) as well

    
    # RETRIEVE VALUE WHEN A KEY IS INPUT
    def get(self, key): 
        index = self.hash(key)

        # Key: value pair doesn't exist
        if self.array[index] is None:
            raise KeyError()
        
        # Key: value pair exists
        else:
            for kvp in self.array[index]:
                if key == kvp[0]:
                    return kvp[1]
            
            # If key not found
            raise KeyError()


queue = HashTable()

queue["person"] = '9'

print(queue['person'])

if "person" in queue:
    print("Phew!")
    print(type(queue["person"]))