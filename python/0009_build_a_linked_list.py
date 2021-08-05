class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    # When linked list is instantiated w/o any elements,
    # head defaults to None
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current = self.head
        values = ""
        while current:
            values += str(current.value) + " "
            current = current.next
        return values

    def append(self, new_element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_pos(self, pos):
        # first pos = 1
        # return None if not found
        element = self.head
        count = 1

        if pos == 1:
            return element
        elif pos > 1 and self.head:
            while count < pos:
                element = element.next
                count += 1
                if element is None:
                    break
            # if (element is not None) else (f"Position {pos} does not exist.") # conditional expression
            return element
        # else:
        #     return None
        return None

    def insert(self, new_element, pos):
        current = self.head
        new_element = Element(new_element)
        count = 1

        if pos == 1:
            new_element.next = current
            self.head = new_element
        # elif not(isinstance(self.get_pos(pos), str)): # use: type(self.get_pos(pos)) == str
        elif pos > 1:
            while count < pos-1:
                current = current.next
                count += 1
            new_element.next = current.next
            current.next = new_element

    def delete(self, value):
        current = self.head
        prev = None

        while current:
            if current.value == value:
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next


e1 = Element(111)
e2 = Element(-35)
e3 = Element(15)

lnk_lst = LinkedList(e1)
lnk_lst.append(e2)
lnk_lst.append(e3)

print(
    f"\nLinked List {lnk_lst} has been created with members {e1.value}, {e2.value}, {e3.value}.")

lnk_lst.insert(277, 4)
print(f"Inserting a number. Now the list is {lnk_lst}")

lnk_lst.insert(-663, 1)
print(f"Inserting a number. Now the list is {lnk_lst}")

lnk_lst.insert(1852, 5)
print(f"Inserting a number. Now the list is {lnk_lst}")

lnk_lst.delete(277)
print(f"Deleting a number. Now the list is {lnk_lst}")

lnk_lst.delete(-35)
print(f"Deleting a number. Now the list is {lnk_lst}")

a = (isinstance(lnk_lst.get_pos(45), int))
print(a)

if (lnk_lst.get_pos(45) is None):
    print("YEAH")

print(lnk_lst.get_pos(4).value)

print(lnk_lst.get_pos(2).value)

'''
# Experiments

# def printLinkedList(self):
#     current = self.head
    
#     while current:
#         print(current.value, end=" ")
#         current = current.next

#     print("\n")

# lnk_lst.insert(-663, 2)
# print(lnk_lst)

# lnk_lst.delete(111)
# print("blah")
# lnk_lst.printLinkedList()



# if e3:  # Object is always true
#     print(1)
'''
