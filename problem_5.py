from time import gmtime
import hashlib

class Block:
    def __init__(self, data, hash_str):
        '''
        This Class creates an individual block for the Linked_Blocks() data structure
        class.
        
        Init Variables:
            self.timestamp = This is the timestamp in Greenwich Mean Time.
            self.data = This is the data the block holds.
            self.hash = This is the unique hash value for the block.
            self.previous = This is the previous block that this block is
                connected to. By default, this value is None.
            self.next = This is the next block that this block is connected to. By
                default, this value is None.
        '''
        
        assert type(hash_str) == str, f"""
        The hash argument is not a string. Please input a string for the hash_str
        argument.
        """
        
        self.timestamp = gmtime()
        self.data = data
        self.hash = self.calc_hash(hash_str)        
        self.previous = None
        self.next = None
    
    def calc_hash(self, the_string):
        '''
        This takes a string value and encodes it with a hash value using
        functions from the imported hashlib module.
        '''
        sha = hashlib.sha256()
        str_encoded = the_string.encode('utf-8')
        sha.update(str_encoded)
        return sha.hexdigest()
    
    def get_hash(self):
        '''
        This function returns self.hash.
        '''
        return self.hash
    
    def get_data(self):
        '''
        This function returns self.data.
        '''
        return self.data
    
    def get_previous(self):
        '''
        This function returns self.previous
        '''
        return self.previous
    
    def get_time(self):
        '''
        This function returns self.timestamp
        '''
        return self.timestamp
    
    def get_next(self):
        '''
        This function returns self.next
        '''
        return self.next
    
    def __repr__(self):
        '''
        When print(Block) is called: This formated value is what is returned.
        '''
        return f"""
        Block(Hash: {self.get_hash()},
              Timestamp: {self.get_time()},
              Data: {self.get_data()})
        """
    
    def __str__(self):
        '''
        When str(Block) is called: This formated value is what is returned.
        '''
        return f"""
        Block(Hash: {self.get_hash()},
              Timestamp: {self.get_time()},
              Data: {self.get_data()})
        """

class Block_Links():
    def __init__(self):
        '''
        This is a linked list data structure that chains blocks from the Block class.
        
        Init Variables:
            Self.head = This is the head of the structure, the first block.
            Self.tail = This is the last block of the structure.
            self.num_elements = This counts the number of elements in the structure.
            self.hash_dict = This is a dictionary that ensures that any appended value
            is a unique value.
        '''
        self.head = None
        self.tail = None
        self.num_elements = 0
        self.hash_dict = {}
    
    def size(self):
        '''
        This returns self.num_elements
        '''
        return self.num_elements
    
    def is_empty(self):
        '''
        This returns True if the data structure is empty, otherwise it returns
        False.
        '''
        return self.size() == 0
    
    def in_hash_dict(self, hash_str):
        '''
        This returns True if a hash code is not in the dictionary, otherwise it
        returns False.
        '''
        return self.hash_dict.get(hash_str) != None
    
    def append(self, data, hash_str):
        '''
        Given that the hash code is not in the hash_dict, this appends a Block
        to the end of Block_Links.
        '''
        
        # This creates the new_block.
        new_block = Block(data, hash_str)
        
        # If the hash code is in the dictionary, this assertion error is returned.
        # Only blocks with unique hash codes can be added to the Block_links structure.
        assert not self.in_hash_dict(new_block.get_hash()), f'''
        This hash code is currently in the hash dictionary. Please choose another
        string value to be converted to a hash code that is unique!
        '''
        
        # This appends the block if the Block_Links structure is empty.
        if self.is_empty():
            self.head = new_block
            self.tail = self.head
            
        # This appends the block to the end of the Block_Links structure, given that
        # the structure isn't empty.
        else:
            temp = self.tail
            previous = temp
            self.tail.next = new_block
            self.tail = self.tail.next
            self.tail.previous = previous
        
        # This updates both the number of elements and the hash dictionary.
        self.num_elements += 1
        self.hash_dict[new_block.get_hash()] = "This unique code is now in the hash_dict"
    
    def get_head(self):
        '''
        This returns the head block if there is one. Otherwise, it returns None.
        '''
        return self.head
    
    def get_tail(self):
        '''
        This returns the tail block if there is one. Otherwise, it returns None.
        '''
        return self.tail
    
    def __repr__(self):
        '''
        This function prints the sequence of blocks when print(Block_Links) is called.
        '''
        
        # If there are no elements within the Block_links structure, this prints
        # an empty structure.
        if self.is_empty():
            return "<Block_Links structure is empty.>"
        
        # If there are elements within the data structure, the code below formats and
        # prints them.
        else:
            # This code prints the head block in the data structure.
            current_block = self.head
            bl_print = "<Head of Block_Links Stucture>\n________________________________\n"
            bl_print += f'''
            Block Hash: {current_block.get_hash()}
            Block Timestamp: {current_block.get_time()}
            Block Data: {current_block.get_data()}
            Previous Block Hash: {current_block.get_previous()}
            '''
            bl_print += "\n________________________________\n"
            current_block = current_block.next
            count = 1
            
            # This code prints all the remaining blocks in the data structure. In the
            # while loop, count refers to an iteration in acomputer science count range,
            # (0, n-1), while self.size is simply n, the number of elements in the
            # Block_Links structure.
            while count < self.size():
                bl_print += f'''
            Block Hash: {current_block.get_hash()}
            Block Timestamp: {current_block.get_time()}
            Block Data: {current_block.get_data()}
            Previous Block Hash: {current_block.get_previous().get_hash()}
            '''
                bl_print += "\n________________________________\n"
                current_block = current_block.next
                count += 1
                
            bl_print += "<Tail of Block_Links Structure>"
            return bl_print
            
# Test Case 1 Setup:
test_1 = Block_Links()
test_1.append("Don\'t forget to bring a towel!", "Towelie")
test_1.append(None, "Towelie - number of brain cells")
test_1.append(3.14, "What Towelie eats when he's feeling good")
# Test Case 1 Data Structure:
print("Below is the Block_Links Structure for test_1.")
print(test_1)
print("______________________________________________\n")

# Test Case 2 Setup:
test_2 = Block_Links()
test_2.append("Portal Gun", "Rick Sanchez")
test_2.append(10, "Jessica")
test_2.append(None, "Morty's chances with Jessica")
# Test Case 2 Data Structure:
print("Below is the Block_Links Structure for test_2.")
print(test_2)
print("______________________________________________\n")

# Test Case 3 Setup
test_3 = Block_Links()
test_3.append("Friend of Maltese Children", "Goosio")
test_3.append("Joe Don Baker", "The worst")
test_3.append("Joe Don Baker", "The best")
# Test Case 3 Data Structure:
print("Below is the Block_Links Structure for test_3.")
print(test_3)
print("______________________________________________\n")

# Test Case 4 Setup and Execution:
# This should result in an error in order to show that the Block Links structure only
# accepts unique hash sting values.
print("test_4 should result in an error. The Block_Links structure only accepts unique hash values.\n")
test_4 = Block_Links()
test_4.append("unique hashes only!", "duplicate hash")
test_4.append("unique hashes only!", "duplicate hash")


# References
# 1. https://en.wikipedia.org/wiki/Blockchain
#2. https://docs.python.org/3/library/time.html#time.struct_time

