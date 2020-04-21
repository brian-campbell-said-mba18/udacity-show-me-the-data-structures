class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.size() == 0
    
    def get_head(self):
        return self.head

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.num_elements += 1
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        self.num_elements +=1

def linked_to_dict(a_linked_list, debug_mode=False):
    '''
    This function returns a dictionary of unique values in a linked list and a count of the 
    number of values in the dictionary.
    '''
    # This raises an error if a linked list is not put into the funcion.
    assert type(a_linked_list) == LinkedList, "This function needs a linked list as input!"
    
    # This raises an error if there is nothing in the linked list.
    assert not a_linked_list.is_empty(), "Please use a linked list that has at least one node."
    
    # This creates the current_node, the unique_values dictionary, and the counter of
    # unique values in the dictionary for the while loop.
    current_node = a_linked_list.get_head()
    unique_values = {}
    unique_counter = 0
    
    # This while loop adds values to the dictionary if a value is not already in the
    # dictionary. It also updates the unique value counter if a new value is appended to
    # the dictionary. The while loop breaks once the current node == None.
    while current_node != None:
        key = current_node.get_value()
        if unique_values.get(key) == None:
            unique_values[key] = "In linked list!!!!"
            unique_counter +=1
            if debug_mode:
                print(f'''
                The key({key}) has a value of 
                ({unique_values[key]}) in the dictionary.
                ___________________________________________________________________________\n
                ''')
        current_node = current_node.next
    
    return unique_values, unique_counter

def intersection(llist_1, llist_2, debug_mode=False):
    '''
    This function returns the intersection linked list of two linked lists.
    '''
    
    # This creates the dictionary and the unique values count for the first linked list.
    dict_1, counter_1 = linked_to_dict(llist_1)
    
    # This creates the dictionary and the unique values count for the second linked list.
    dict_2, counter_2 = linked_to_dict(llist_2)
    
    # This conditional determines which dictionary is smaller. Once that is determined, the 
    # small dictionary will be used to query the larger dictionary. It is acceptable if
    # both dictionaries are the same size.
    if counter_1 <= counter_2:
        small = dict_1
        big = dict_2
    else:
        small = dict_2
        big = dict_1
        
    # This initiates the intersection linked list set.
    intersection_output = LinkedList()
    
    for key in small:
        try:
            small[key] == big[key]
            intersection_output.append(key)
            if debug_mode:
                print(f'''
                Key: ({key}) in both dictionaries! TRUE! This key was appended to the intersection
                linked_list output.
                ____________________________________________________________________________\n
                ''')
            
        except KeyError:
            if debug_mode:
                print(f'''
                Key: ({key}) not in both dictionaries. FALSE! NOTHING APPENDED!
                ____________________________________________________________________________\n
                ''')
    
    # If the intersection_output is empty, this function returns none.
    if intersection_output.is_empty():
        return None
    
    # If the intersection_output set is not empty, this function returns the intersection output.
    return intersection_output

def union(llist_1, llist_2, debug_mode=False):
    '''
    This function returns the union linked list of two linked lists.
    '''
    
    # This creates the dictionary and the unique values count for the first linked list.
    dict_1, counter_1 = linked_to_dict(llist_1)
    
    # This creates the dictionary and the unique values count for the second linked list.
    dict_2, counter_2 = linked_to_dict(llist_2)
    
    # This conditional determines which dictionary is smaller. Once that is determined, the 
    # small dictionary will be used to query the larger dictionary. It is acceptable if
    # both dictionaries are the same size.
    if counter_1 <= counter_2:
        small = dict_1
        big = dict_2
        big_counter = counter_2
    else:
        small = dict_2
        big = dict_1
        big_counter = counter_1
        
    # This initiates the union linked list set.
    union_output = LinkedList()
    
    # This for loop appends everything from the small dictionary into the union linked list.
    # It also delete entries out of the big dictionary.
    for key in small:
        try:
            small[key] == big[key] # Boolean Query, if false, we go to except KeyError
            union_output.append(key)
            del big[key] # Entry deleted from the big dictionary. Code from Reference 1 in References.
            big_counter -= 1 # Big dictionary counter -1.
            if debug_mode:
                print(f'''
                Key: ({key}) in both dictionaries! TRUE! This key was appended to the union
                linked list output.
                ____________________________________________________________________________\n
                ''')
            
        except KeyError:
            union_output.append(key)
            if debug_mode:
                print(f'''
                Key: ({key}) only in the small dictionary. This key was appended to the
                union linked list output.
                ____________________________________________________________________________\n
                ''')
    
    # This for loop is activated if there are remaining values in the big dictionary.
    if big_counter > 0:
        if debug_mode:
            print(f'''
            Starting new loop. Appending the remaining {big_counter} values from the BIG
            dictionary.
            ____________________________________________________________________________\n
            ''')
        for key in big:
            union_output.append(key)
            big_counter -= 1
            if debug_mode:
                  print(f'''
                  Appended key ({key}) to the union linked list output. Remaining number of
                  values: {big_counter}.
                  ____________________________________________________________________________\n
                  ''')
            
    # If the union_output is empty, this function returns none.
    if union_output.is_empty():
        return None
    
    # If the intersection_output set is not empty, this function returns the intersection output.
    return union_output

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print("Test Case 1: Union")
print (union(linked_list_1,linked_list_2), '\n')
print("Test Case 1: Intersection")
print (intersection(linked_list_1,linked_list_2))
print("_______________________________________________________\n")

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()


element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]


for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Test Case 2: Union")
print (union(linked_list_3,linked_list_4), '\n')
print("Test Case 2: Intersection")
print (intersection(linked_list_3,linked_list_4))
print("_______________________________________________________\n")

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()


element_5 = ["roy", "g", "biv", 3.14, 5, 2, 1]
element_6 = ["roy", "g", "biv", 5, 1, "Happy Dance"]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print("Test Case 3: Union")
print (union(linked_list_5,linked_list_6), '\n')
print("Test Case 3: Intersection")
print (intersection(linked_list_5,linked_list_6))
print("_______________________________________________________\n")

# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()


element_7 = ["the", "illuminati", "is", "watching", None, None, None]
element_8 = ["the", "illuminati", None, "is", "the", "CIA", 3.14]

for i in element_7:
    linked_list_7.append(i)

for i in element_8:
    linked_list_8.append(i)

print("Test Case 4: Union")
print (union(linked_list_7,linked_list_8), '\n')
print("Test Case 4: Intersection")
print (intersection(linked_list_7,linked_list_8))
print("_______________________________________________________\n")

# References
# 1. https://www.hackerearth.com/practice/python/working-with-data/dictionary/tutorial/