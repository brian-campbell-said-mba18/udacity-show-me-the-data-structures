class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

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
        self.p = 31
        self.num_entries = 0
    
    def round_up(self, some_number):
        if some_number % 1 == 0:
            return int(some_number)
        else:
            return int((some_number + 1) // 1)

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
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

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)         # we can use our put() method to rehash
                head = head.next
                
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

stupid = LRU_HashMap(25)
print(stupid.array_size)


# References
# 1. Udacity: Data Structures & Algorithms Nanodgree; 2. Data Structures; Lesson 5: Maps and Hashing; 8. Hash Maps Notebook