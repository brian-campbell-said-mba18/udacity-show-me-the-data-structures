class LinkedListNode:
    
    def __init__(self, key, value, version=1):
        self.key = key
        self.value = value
        self.version = version
        self.next = None
        # This code comes from Reference 1 of References, verbatim.
    

    def __repr__(self):
        '''
        This function returns the string value format when
        print(LinkedListNode) is called.
        '''
        return f"Node(Key: {self.key}, Value: {self.value}, Version: {self.version})"
        # This code comes from Reference 2 of References.
    
    def __str__(self):
        '''
        This function returns the string value format when
        str(LinkedListNode) is called.
        '''
        return f"Node(Key: {self.key}, Value: {self.value}, Version: {self.version})"
        # This code comes from Reference 2 of References.  

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enq(self, entered_node):
        new_node = entered_node
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements +=1

    def deq(self):
        if self.size() == 0:
            return 
        temp = self.head
        self.head = self.head.next
        self.num_elements -=1
        return temp

    def size(self):
        return self.num_elements

    def print_queue(self):
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
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                head.version += 1
                new_node.version = head.version
                print(f"""
                {head} modifed,
                LRU node version = {head.version}!
                Entry Record Node version = {new_node.version}!
                ______________________________________\n\n""")
                self.entry_record.enq(new_node)
                self.entry_record.print_queue()
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        self.entry_record.enq(new_node)
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        self.entry_record.print_queue()
        
        # check for overcapacity
        if self.size() > self.capacity:
            # self.num_entries = 0
            self.make_room()
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    def get_version(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.version
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
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
        return self.num_entries

    def make_room(self):
        while True:
            if self.entry_record.size() == 0:
                print(f"""Entry record empty, breaking loop now!
                ________________________________________________""")
                break
            temp = self.entry_record.deq()
            print(f"""Popped {temp},
            from entry record. Searching for
            matching Node to delete in
            the LRU Cache Structure...
            ...
            """)
            if self.get(temp.key) == temp.value:
                if self.get_version(temp.key) == temp.version:
                    self.delete(temp.key)
                    print(f"""Entry record equals LRU record.
                    VICTORY IS OURS! Breaking the loop! 
                    ___________________________________""")
                    break
            print(f"""The entry record did not match the LRU
                Cache Node. RESTARTING the loop!
                ________________________________________________\n\n""")
                
    def delete(self, key):
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

stupid = LRU_HashMap(5)
stupid.set("one",1)
stupid.set("two", 2)
stupid.set("one",0)
#stupid.set("four", 4)
#stupid.set("five", 5)
#stupid.set('six', 7)
#temp = stupid.entry_record.deq()
#print(temp.key)
#stupid.entry_record.print_queue()

'''
idiot_queue = Queue()
node_1 = LinkedListNode("idiot", 1, 1)
node_2 = LinkedListNode("idiot", 2, 2)
node_3 = LinkedListNode("idiot", 3, 3)
idiot_queue.enq(node_1)
idiot_queue.enq(node_2)
idiot_queue.enq(node_3)
idiot_queue.print_queue()
'''

# References
# 1. Udacity: Data Structures & Algorithms Nanodgree; 2. Data Structures; Lesson 5: Maps and Hashing; 8. Hash Maps Notebook
# 2. Udacity: Data Structures & Algorithms Nanodgree; 2. Data Structures; Lesson 4: Trees; 14. Code: BFS

