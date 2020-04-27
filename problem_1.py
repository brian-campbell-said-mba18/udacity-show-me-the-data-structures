class LinkedListNode:
    
    def __init__(self, key, value, num_of_edits=0):
        '''
        This is the node value class to be used by the Queue() and LRU_Hashmap() data structures.

        This code comes from Reference 1 in References.
        '''
        self.key = key
        self.value = value
        self.num_of_edits = num_of_edits
        self.next = None

    def __repr__(self):
        '''
        This function returns the string value format when print(LinkedListNode) is called.
        '''
        return f"Node(Key: {self.key}, Value: {self.value}, Num_of_edits: {self.num_of_edits})"
        # This code comes from Reference 2 of References.
    
    def __str__(self):
        '''
        This function returns the string value format when str(LinkedListNode) is called.
        '''
        return f"Node(Key: {self.key}, Value: {self.value}, Num_of_edits: {self.num_of_edits})"
        # This code comes from Reference 2 of References.  

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enq(self, entered_node):
        '''
        This adds a node to the back of the queue.
        '''
        new_node = entered_node
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements +=1

    def deq(self):
        '''
        This deletes the node at the front of the queue.
        '''
        if self.size() == 0:
            return 
        temp = self.head
        self.head = self.head.next
        self.num_elements -=1
        return temp

    def size(self):
        '''
        This returns the number of elements in the queue.
        '''
        return self.num_elements

    def print_queue(self):
        '''
        This function prints the queue and its contents.
        '''
        print(f"""
        <dequeue AKA remove>
        ________________________________""")
        node = self.head
        while node != None:
            print(f"""
            {node}
            ________________________________""")
            node = node.next
        print(f"""
        <enqueue AKA add>\n""")

class LRU_HashMap:
    
    def __init__(self, capacity=5, load_factor=0.7):
        '''
        This sets the inital variables for the class.
        Variable Descriptions:
            self.capacity - How many items can be in the bucket array. 5 is the default.
            self.load_factor - The maximum limit of capacity / bucket array size, 0.7 by default.
            self.array_size - The greatest bucket array size that makes the load factor <= 0.7.
            self.bucket_array - This is where the nodes of keys and values are stored.
            self.p - This is the prime number, 31, that's used for creating the hash code.
            self.num_entries - This is a counter of how many nodes are currently in self.bucket_array.
        '''
        self.capacity = capacity
        self.load_factor = load_factor
        self.array_size = self.round_up(capacity / load_factor)
        self.bucket_array = [None for _ in range(self.array_size)]
        self.entry_record = Queue()
        self.p = 31
        self.num_entries = 0
        # Code and information regarding load factor comes from Reference 1 of References.
    
    def round_up(self, some_number):
        '''
        Disclaimer: This is a helper funciton. It is not usually meant to be called upon.

        Function Purpose: This function rounds up a numerical value. If the value is an
        integer, that integer is returned. Otherwise, the value is rounded up. This
        function is used to ensure that the array size is large enough so the load factor
        does not exceed 0.7.
        '''
        if some_number % 1 == 0:
            return int(some_number)
        else:
            return int((some_number + 1) // 1)

    def set(self, key, value):
        '''
        This either adds a new node to the LRU Hashmap or it modifies an exisiting node. 
        Also, if the LRU Hashmap gets too big, the make room function is called and the
        oldest node is deleted from the Hashmap.

        This code comes from Reference 1 in References.

        Commented Out Print Statements: The print statements were used for debugging purposes.
        Feel free to uncomment them to debug.
        '''
        bucket_index = self.get_bucket_index(key)
        entry_node = LinkedListNode(key, value)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        # This also adds an entry node to the self.entry_record queue.
        while head is not None:
            if head.key == key:
                head.value = value
                head.num_of_edits += 1
                entry_node.num_of_edits = head.num_of_edits
                # Below print function is used for debugging purposes.
                #print(f"""
                #{head} modifed,
                #LRU node # of edits = {head.num_of_edits}.
                #Entry Record Node # of edits = {entry_node.num_of_edits}.
                #______________________________________\n\n""")
                entry_node.num_of_edits = head.num_of_edits
                self.entry_record.enq(entry_node)
                # The print_queue function below is for debugging purposes.
                #self.entry_record.print_queue()
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        # This also adds an entry node to the self.entry_record queue.
        self.entry_record.enq(entry_node)
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        # The print_queue function below is for debugging purposes.
        # self.entry_record.print_queue()
        
        # check for overcapacity
        if self.size() > self.capacity:
            self.make_room()
        
    def get(self, key):
        '''
        This returns the value of a search node if it exists. Otherwise this function returns none.

        This code comes from Reference 1 in References.
        '''

        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                head.num_of_edits += 1
                entry_node = LinkedListNode(key, head.value, head.num_of_edits)
                self.entry_record.enq(entry_node)
                return head.value
            head = head.next
        return -1
        
    def make_get(self, key):
        '''
        WARNING: Do not manually activate this function! It is only for the make_room() funciton.

        This returns the value of a search node if it exists. Otherwise this function returns none.

        This code comes from Reference 1 in References.
        '''

        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return -1
    
    def make_get_edits(self, key):
        """
        WARNING: Do not manually activate this function! It is only for the make_room() funciton.

        This returns the number of edits of an existing node within the LRU Hashmap structure.

        This code comes from Reference 1 in References.
        """
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.num_of_edits
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        '''
        This returns the bucket index in order to query. The bucket index is used to query the
        bucket array for setting and getting nodes.

        This code comes from Reference 1 in References.
        '''
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        '''
        This returns the hash code for a key.

        This code comes from Reference 1 in References.
        '''
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient
        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        '''
        This returns the number of entries within the LRU Hashmap.
        '''
        return self.num_entries

    def make_room(self):
        '''
        When a Node is added to the LRU data structure that causes overcapacity, this function
        querries the entry record queue to find the oldest node within the LRU data structure. 
        Once the value of the node matches a node within the LRU hashmap structure, the LRU
        node is removed from the LRU structure.

        Commented Out Print Statements: The print statements were used for debugging purposes.
        Feel free to uncomment them to debug.
        '''
        while True:
            if self.entry_record.size() == 0:
                #print(f"""
                #Entry record empty, breaking loop now!
                #__________________________________________""")
                break
            temp = self.entry_record.deq()
            #print(f"""
            #Popped {temp},
            #from entry record. Searching formatching Node 
            #to delete in the LRU Cache Structure...
            #...
            #""")
            if self.make_get(temp.key) == temp.value:
                if self.make_get_edits(temp.key) == temp.num_of_edits:
                    self.delete(temp.key)
                    #print(f"""
                    #Entry record equals LRU record. LRU Node deleted.
                    #Succeess! BREAKING the loop! 
                    #__________________________________________""")
                    break
            #print(f"""
            #The entry record did not match the LRU
            #Cache Node. RESTARTING the loop!
            # __________________________________________\n\n""")
                
    def delete(self, key):
        '''
        This function removes a Node from the LRU Hashmap.

        This code comes from Reference 1 in References.
        '''
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

# Test Case 1: This case edits a lot of values making it more difficult for the LRU_Hashmap Class
# to identify the Least Recently Used Cache.
print("Starting Test Case 1.\n")
test1 = LRU_HashMap(5)
test1.set("one",1)
test1.set("two", 2)
test1.set("one",0)
test1.set("two", 42)
test1.set("one",3)
test1.set("one",2)
test1.set("three", 234)
test1.set("four", 4)
test1.set("five", 5)
test1.set('six', 7)

print(test1.get("two")) # This should print -1.
print(test1.get("one")) # This should print 2.
print(test1.get("six")) # This should print 7.
print("Moving onto Test Case 2.")
print("________________________________________\n")

# Test Case 2: This is simply the Udacity Test Case from the boilerplate code for project 1, this project.
our_cache = LRU_HashMap(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("Moving onto Test Case 3.")
print("________________________________________\n")

# Test Case 3 Setup: This is simply the Udacity Test Case from the boilerplate code for project 1, this project.
# However, I modified the first two nodes and gave them None as values for an edge case.
test3 = LRU_HashMap()

test3.set(1, None)
test3.set(2, None)
test3.set(3, 3)
test3.set(4, 4)


print(test3.get(1))       # returns None
print(test3.get(2))       # returns None
print(test3.get(9))      # returns -1 because 9 is not present in the cache

test3.set(5, 5) 
test3.set(6, 6)

print(test3.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("Moving onto Test Case 4.")
print("________________________________________\n")

# Test Case 4 Setup: This is an edge case in which the hashmap is empty.
test4 = LRU_HashMap()

print(test4.get(1))       # returns -1
print(test4.get(2))       # returns -1
print(test4.get(9))      # returns -1 

print("Moving onto Test Case 5.")
print("________________________________________\n")

# Test Case 5 Setup: This is an edge case in the first entry into the LRU_Hashmap is a large number.
test5 = LRU_HashMap()
test5.set(758230958713095, "hello")
test5.set(1, "Two")
test5.set("Buckle", "my")
test5.set("Shoe", "lace")

print(test5.get(758230958713095)) # returns "hello"
print(test5.get("Buckle")) # returns "my"

test5.set(2, "blue")
test5.set("fish", "and chips")

print(test5.get(1)) # returns -1 because this entry was deleted from the Cache.

print("End of Test Cases!")
print("________________________________________")


# References
# 1. Udacity: Data Structures & Algorithms Nanodgree; 2. Data Structures; Lesson 5: Maps and Hashing; 8. Hash Maps Notebook
# 2. Udacity: Data Structures & Algorithms Nanodgree; 2. Data Structures; Lesson 4: Trees; 14. Code: BFS

