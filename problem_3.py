class Node:
    '''
    This class serves as the node for the tree class.
    
    Init Values:
        self.character - This is the string character to be encoded.
        self.frequency - This is the frequency of the string character.
        self.previous - This references the parent node, if there is one.
        self.left_child - This references the left child node, if there is one.
        
    References: All the get and has functions comes from Reference 2 of References. The set
                funcitons come from Reference 3.
    '''
    def __init__(self, frequency, character = None):
        # An error is raised if frequency is not an integer value.
        assert type(frequency) == int, "Self.frequency must be an integer!"
        self.frequency = frequency
        self.character = character
        self.huff_code = None
        self.left_child = None
        self.right_child = None
    
    def has_character(self):
        '''This boolean is True if the Node has a character and false otherwise.'''
        return self.character != None
    
    def set_huff_code(self, value):
        ''' This sets the huffman code for the node'''
        self.huff_code = value
    
    def get_character(self):
        '''This returns self.character.'''
        return self.character
    
    def get_frequency(self):
        '''This returns self.frequency.'''
        return self.frequency
    
    def get_huff_code(self):
        '''This returns self.huff_code.'''
        return self.huff_code
    
    def get_left_child(self):
        '''This returns self.left_child.'''
        return self.left_child
    
    def has_left_child(self):
        '''Returns True/False, is there a left child?'''
        return self.get_left_child() != None
    
    def set_left_child(self, node):
        '''This function takes in the argument node and assigns self.left_child to it.'''
        assert type(node) == Node, "This function needs a node as an argument."
        self.left_child = node
    
    def get_right_child(self):
        '''This returns self.right_child'''
        return self.right_child
    
    def has_right_child(self):
        '''Returns True/False, is there a right child?'''
        return self.get_right_child() != None
    
    def set_right_child(self, node):
        '''This function takes in the argument node and assigns self.right_child to it.'''
        assert type(node) == Node, "This function needs a node as an argument."
        self.right_child = node
        
    def __repr__(self):
        '''This is what is returned when print(Node) is called.'''
        return f'Node({self.frequency})'
    
    def __str__(self):
        '''This is what is returned when str(Node) is called.'''
        return f'Node({self.frequency})'


class Tree:
    '''
    This is the tree class which consists of nodes. Every node in the tree can have a left and 
    right child.
    '''
    def __init__(self, root=None):
        '''
        Init Variables:
            self.root - This is the root node; it is the top of the tree. Initially, the root
            node is set to None.
        '''
        # An error is raised if the root isn't a Node or none
        assert (type(root) == Node) or (root == None), f'''The initial root needs to either be
        a Node or None.'''
        self.root = root
    
    def get_root(self):
        '''This returns the root node or none if there isn't a root node.'''
        return self.root
    
    def set_root(self, root):
        '''This sets the root node.'''
        assert type(root) == Node, "This function needs a node to set the root!"
        self.root = root
    
    def __repr__(self):
        '''This is what is returned when print(Tree) is called.'''
        return f"Tree(Root({self.root}))"
    
    def __str__(self):
        '''This is what is returned when str(Tree) is called.'''
        return f"Tree(Root({self.root}))"

class Stack_Node():
    '''
    This is a very purposefuly a rudimentary node for the priority stack. It is only meant to
    contain information. The priority stack class consists of these nodes.
    
    self.data: This data should only be Nodes or Trees.
    '''
    
    def __init__(self, data):
        '''
        Init Variables:
            self.data - The data in the node. This data should only be Nodes or Trees.
            self.next - The next node, if there is one (set to None by default).
        '''
        assert (type(data) == Node) or (type(data) == Tree), f'''The data needs to be in the form
        of a node or tree.'''
        self.data = data
        self.next = None
        self.previous = None
        
    def get_data(self):
        '''This returns self.data.'''
        return self.data
    
    def set_data(self, data):
        '''This sets the data for the node, which should come in the form of a Node or Tree.'''
        assert (type(data) == Node) or (type(data) == Tree), f'''The data needs to be in the form
        of a node or tree.'''
        self.data = data
        
    def __repr__(self):
        '''This is what is returned when print(Stack_Node) is called.'''
        return f"Stack_Node({self.data})"
    
    def __str__(self):
        '''This is what is returned when str(Stack_Node) is called.'''
        return f"Stack_Node({self.data})"

class Priority_Stack:
    ''' The purpose of the priority stack is to hold the stack nodes that will help build the
    Huffman Tree.'''
    
    def __init__(self, head=None):
        '''
        Init Variables:
            self.head = The top of the stack.
            self.elements_in_stack = The number of elements in the stack.
        '''
        # An error is raised if head is not None or not a Stack Node.
        assert (type(head) == Stack_Node) or (head == None), f'''Self.bottom must be a 
        Stack_Node or None.'''
        self.head = head
        
        # This conditional statement initiates self.elements_in_stack.
        if self.head != None:
            self.elements_in_stack = 1 # If self.head initiated, this is 1.
        else:
            self.elements_in_stack = 0 # If self.head not initiated, this is 0.
        
    def stack_size(self):
        '''This returns self.elements_in_stack.'''
        return self.elements_in_stack
    
    def is_stack_empty(self):
        '''This returns True if the stack is empty, False if it is not.'''
        return self.stack_size() < 1
    
    def push(self, add_stack_node):
        '''This adds Stack Nodes to the stack.'''
        assert type(add_stack_node) == Stack_Node, 'Only Stack_Nodes can be pushed onto the stack.'
        
        # This conditional pushes the value onto the top of the stack. It either initiates a 
        # self.head for an empty stack, or it creates a new top of the stack.
        if self.is_stack_empty():
            self.head = add_stack_node
        else:
            self.head.next = add_stack_node
            add_stack_node.previous = self.head
            self.head = self.head.next
        
        # The number of elements in the stack is updated.
        self.elements_in_stack += 1
        
    def pop(self):
        '''
        This deletes a value from the top of the stack and returns it, if there is anything
        in the stack.
        '''
        # Nothing is deleted if the stack is empty.
        if self.is_stack_empty():
            print("Stack is empty, nothing to pop")
            return None
        
        # If the stack has elements, the top is popped and returned. A new top, self.head
        # is assigned.
        temp = self.head
        self.head = self.head.previous
        self.elements_in_stack -= 1
        return temp
    
    def priority_insert(self, stakk_node):
        '''
        Function PUrpose:
            This is used to maintain a specific order in the stack. The largest value is on the
            bottom, while the smallest value is on the top. However, this function will fail in
            maintaining this order if values have been pushed in randomly and the order is already
            random. In order to initiate and maintain the desired order, only use priority insert
            when inserting values, DO NOT, use the push() function.
        '''
        # An error is raised stakk_node is not a Stack_Node().
        assert type(stakk_node) == Stack_Node, "Error! This function only inserts Stack_Nodes!"
        
        # If the stack is empty, this initiates the first element in the stack.
        if self.is_stack_empty():
            self.head = stakk_node
            self.elements_in_stack +=1
            return
        
        # If the stack node to add is less than the element at the top of the stack,
        # this makes the value the new top of the stack.
        if stakk_node.get_data().get_frequency() <= self.head.get_data().get_frequency():
            self.head.next = stakk_node
            stakk_node.previous = self.head
            self.head = self.head.next
            self.elements_in_stack +=1
            return
        
        # These variables keep track of the stack node higher in the stack and the stack node 
        # lower in the stack, higher and current, for the use of the while loop below.
        higher = self.head
        current = self.head.previous
        
        # Unless the stack node to add is greater than the bottom stack node, this while loop 
        # inserts the new stack node in the stack.
        while current != None:
            if stakk_node.get_data().get_frequency() <= current.get_data().get_frequency():
                current.next = stakk_node
                stakk_node.previous = current
                higher.previous = stakk_node
                stakk_node.next = higher
                self.elements_in_stack +=1
                return
            higher = higher.previous
            current = current.previous
        
        # If the new stack node is greater than the bottom stack node, then the new stack node
        # is added and becomes the new bottom of the stack.
        higher.previous = stakk_node
        stakk_node.next = higher
        self.elements_in_stack +=1
        return
    
    def priority_del(self):
        '''Function Purpose: This deletes twos stack node from the priority queue and combines
                them into one new stack node. This function is used for the creation of a huffman
                tree.
        '''
        # An error is raised if the stack size is not 2 or greater.
        assert self.stack_size() > 1, f'''Error, the stack size must be at least 2 to execute this
        function.'''
        
        # This pops the stack nodes and creates the left node and the right node, which will
        # serve as the left and right child of the output node.
        popped_left_stacknode = self.pop()
        node_left = popped_left_stacknode.get_data()
        popped_right_stacknode = self.pop()
        node_right = popped_right_stacknode.get_data()
        
        # This creates the new node from the sum of the frequencies of node_left and node_right.
        new_node = Node(node_left.get_frequency() + node_right.get_frequency())
        
        # This sets the left and right children of the new node, stores it into a stack node,
        # and returns the stack node.
        new_node.set_left_child(node_left)
        new_node.set_right_child(node_right)
        output_stack_node = Stack_Node(new_node)
        return output_stack_node
        
    def last_2_stacknodes(self):
        # An error is raised if the size of the priority stack is not 2 exactly.
        assert self.stack_size() == 2, f'''This function only works when the priority stack size
        is exactly two.'''
        
        # This pops the stack nodes and creates the left node and the right node, which will
        # serve as the left and right child of the root of the output tree.
        popped_left_stacknode = self.pop()
        node_left = popped_left_stacknode.get_data()
        popped_right_stacknode = self.pop()
        node_right = popped_right_stacknode.get_data()
        
        # This creates the new node from the sum of the frequencies of node_left and node_right.
        # This node is then stored in a tree.
        new_node = Node(node_left.get_frequency() + node_right.get_frequency())
        
        # This sets the left and right children of the new node, stores it into a tree node,
        # stores the tree into a stack node, and then returns the output_stack_node.
        new_node.set_left_child(node_left)
        new_node.set_right_child(node_right)
        new_tree = Tree(new_node)
        output_stack_node = Stack_Node(new_tree)
        return output_stack_node
    
    def return_the_tree(self):
        ''' This pops the last stack node out of the stack and converts it to a Tree.'''
        assert self.stack_size(), f'''This only works when the stack size is 1! The current stack
        size is ({self.stack_size}).
        '''
        output_stacknode = self.pop()
        output = output_stacknode.get_data()
        
        # If the element in the stack node is a node, this converts it to a tree.
        if type(output) == Node:
            output_tree == Tree(output)
            return output_tree
        
        # If there was no need for a node to tree conversion, the output (in tree form) is
        # returned.
        return output
    
    def frequency_tree(self, debug_mode = False):
        '''
        Function Purpose: This function converts a priority stack to a frequency tree.
        
        Returns: Frequency Tree
        '''
        # An error is raised if the priority stack is empty.
        assert not self.is_stack_empty(), "Stack is empty, nothing to return."
        
        # This returns the output tree when there is only one node in the priority stack.
        if self.stack_size() == 1:
            if debug_mode:
                print('We are dealing with only 1 Stack Node in the Priority Stack...')
            
            # This pops the last stack node of the priority stack and extracts either a node or a
            # tree.
            last_stacknode = self.pop()
            output = last_stacknode.get_data()
            
            # If output == Node, it is converted to a tree.
            if type(output) == Node:
                output_tree = Tree(output)
                if debug_mode:
                    print("Output was a node, but it was converted to a tree! Success!")
                return output_tree
        
            #If the output was already a tree, it is simply returned.
            if debug_mode:
                print('Ouput was already a tree. Success!')    
            return output
        
        # This returns the output when there are two or more stacknodes in the priority stack.
        # This while loop keeps combining stacknodes and adding them to the priority stack until
        # there are only two stacknodes left.
        if debug_mode:
            print(f'''
            There are {self.stack_size()} Stack Nodes in the Priority Stack...\n''')
        while self.stack_size() > 2:
            if debug_mode:
                print(f'''
                IN WHILE LOOP: The stack size is ({self.stack_size()}) which is greater than 2...
                ''')
            condensed_stacknode = self.priority_del()
            self.priority_insert(condensed_stacknode)
            if debug_mode:
                print(f'''
                The Condensed Stack Node ({condensed_stacknode}) was created and added to the
                Priority Stack. The stack size is now ({self.stack_size()})\n
                ''')
        
        # With the while loop finished, this code returns the output tree.
        final_stacknode = self.last_2_stacknodes()
        self.priority_insert(final_stacknode)
        freq_tree_output = self.return_the_tree()
        if debug_mode:
            print(f'''
            OUT OF THE WHILE LOOP: Created the frequency tree: ({freq_tree_output}). Success!
            ''')
        return freq_tree_output
    
    def __repr__(self):
        '''This is what is returned when the print(Priority_Stack) is called.'''
        
        if self.is_stack_empty(): # Below is what is returned when the stack is empty.
            return f"<Empty Stack>"
        
        # If the stack isn't empty, the below code prints the stack, in the print_message.
        print_message = f'''
        <Top of Stack: Push/Pop>
        _______________________________
        '''
        
        # The current node is set to the top of the stack for the while loop below.
        current_node = self.head
       
        # We use a while loop to print all the nodes from the top to the bottom of the stack.
        while current_node != None:
            print_message += f'''
            {current_node}
            _______________________________
            '''
            current_node = current_node.previous 
        
        # The loop is broken, and we add <bottom of stack> to the print message.
        print_message += f'''
        <Bottom of Stack>
        '''
        return print_message

def str_to_dict(the_string):
    '''
    The purpose of this function is create a dictionary from the string. The keys
    of the dictionary are the unique characters in the string. The values are frequencies
    in which these unique characters occur.
    
    Function Argument: A string of at least 1 character in length.
    
    The function returns: The dictionary of unique characters as keys, and the frequency counts
    as values.
    '''
    # This asserts that function argument is a string.
    assert type(the_string) == str, "The sole argument must be a string!"
    
    # This asserts that the argument is a string that has a length of at least 1.
    assert len(the_string) > 0, "String argument must have at least 1 character."
    
    # This initates the frequency dictionary.
    frequency_dict = {}
    
    # The for loop either (if) initally adds the unique character with a frequency count of 1, 
    # or (else) updates the unique character by adding 1.
    for i in the_string:
        if frequency_dict.get(i) == None:
            frequency_dict[i] = 1
        else:
            frequency_dict[i] += 1
    
    # This returns the frequency dictionary.
    return frequency_dict

def dict_to_tuples(the_dict):
    '''
    This function is specifically built to convert the output of the str_to_dict() function.
    
    Argument: The dictionary output from str_to_dict().
    
    What the function does: In a for loop, the key and values of the argument dictionary
    are converted into a tuple: (key, value), which is then appended to a list.
    
    Returns: A list of tuples. For each tuple item, the first element is the string character and
    the second element is the frequency count.
    '''
    output_list = [] # This initiates the output list.
    
    # The for loop below converts keys and values to tuple items in the output_list.
    for key, value in the_dict.items():
        x = (value, key)
        output_list.append(x)
    
    # This returns the output_list.
    return output_list

def tuples_to_stacknodes(the_list):
    '''
    Function Purpose:
        The purpose of this function is to take a list of tuples of frequency and characters
        and convert them to stack nodes to be put into the priority stack.
        
    Returns: A list of stack nodes.
    '''
    stack_node_list = []
    for i in the_list:
        freq, char = i[0], i[1]
        stack_node = Stack_Node(Node(freq, char))
        stack_node_list.append(stack_node)
    
    return stack_node_list

def stacknodes_to_freq_tree(some_stacknodes):
    '''
    Function Purpose: The purpose of this function is to convert the Stack Nodes to a frequency
            tree.
    Returns: A Frequency Tree
    '''
    
    # This puts the Stack Nodes into the Priority Stack.
    p_stack = Priority_Stack()
    for i in some_stacknodes:
        p_stack.priority_insert(i)
    
    # This converts the priority stack to a frequency tree.
    freq_tree = p_stack.frequency_tree()
    return freq_tree

def str_to_freq_tree(a_string):
    '''
    Function Purpose: This takes a string and puts it into a frequency tree.
    
    Returns: A frequency tree.
    '''
    if len(a_string) == 0:
        frequency_tree = Tree(Node(0, ''))
        return frequency_tree
    # This converts the a_string to a dictionary that counts the frequency of a character in the
    # string.
    the_dict = str_to_dict(a_string)
    
    # This converts the dictionary of characters and frequencies to a list of tuples with the
    # order of (frequency, character).
    tuples = dict_to_tuples(the_dict)
    
    # This converts the tuple list to a list of Stack Nodes.
    stack_nodes = tuples_to_stacknodes(tuples)
    
    # This converts the list of Stack Nodes to a frequency tree and returns the tree.
    frequency_tree = stacknodes_to_freq_tree(stack_nodes)
    return frequency_tree

def huffman_recursion(node, huff_code ='', debug_mode = False):
    '''
    Function Purpose: This function recursively adds binary values to each each node that hasa character within a tree.
    
    Returns: It modifies the tree that is input into the function. It adds huffman code values to all nodes that have a
        character.
        
    References: The idea for this function came from Reference 4 of References.
    '''
    
    # This ensures that all the recursive functions have debug mode turned on/off.
    debug_setting = debug_mode
    
    # This is the base case. In the base case, binary huffman code is added to a node that has a character.
    if node.has_character():
        node.set_huff_code(huff_code)
        if debug_mode:
            print(f'''
            ({node}) with character ({node.get_character()}) now has the huffman code:
            ({node.get_huff_code()})
            ''')
        return
    
    # If the base case is not found, this creates the child list that the for loop below will use to search for nodes with
    # characters in them.
    left_child = node.get_left_child()
    left_huff = huff_code + '0'
    right_child = node.get_right_child()
    right_huff = huff_code + '1'
    child_list = [(left_child, left_huff), (right_child, right_huff)]
    
    if debug_mode:
        print(f'''
        Exploring the children of parent {node}. The left child is {left_child} with a current
        huffman code of ({left_huff}). The right child is {right_child} with a current huffman
        code of ({right_huff}).
        ''')
    
    # The for loop is activated and it uses the recursive function to continue either adding huffman codes to qualified
    # nodes or creating more recursive for loops.
    for i in child_list:
        huffman_recursion(i[0], i[1], debug_setting)
    
    return

def prime_huffman_function(root, huff_code = "", debug_mode = False):
    '''
    Function Purpose: This function either identifies the edge case when there is only one string character, or it runs the
    recursive huffman function, huffman_recursion.
    '''
    
    # This is the edge case when the frequncy count of the root node is 1.
    if root.get_frequency() == 1:
        root.set_huff_code('0')
        if debug_mode:
            print(f'''
            This is an edge case in which there is only one character in the string...\n
            The root: {root}, with the character of ({root.get_character()}) now has a huffman code of ({root.get_huff_code()}).
            ''')
        return

    # This is for all other cases in which the frequency count of the root node is not equal to 1.
    debug_setting = debug_mode
    huff_initial = huff_code
    first_node = root
    huffman_recursion(first_node, huff_initial, debug_setting)
    return


import sys

# Test Case 1
print(f'''
Start Test Case 1...
''')
test_string = "Happy Day"
test_tree = str_to_freq_tree(test_string)
root_of_test_tree = test_tree.root
prime_huffman_function(root_of_test_tree, debug_mode=True)
print('''
End Test Case 1, begin Test Case 2.
''')

# Test Case 2: This is the edge case with nothing in the string.
print(f'''
Start Test Case 2...
''')
test_tree2= str_to_freq_tree("")
root_2 = test_tree2.root
prime_huffman_function(root_2, debug_mode=True)
print('''
End Test Case 2, begin Test Case 3.
''')

# Test Case 3: This is an edge case with only one character.
test_tree3 = str_to_freq_tree("1")
root3 = test_tree3.root
prime_huffman_function(root3, debug_mode=True)
print('''
End Test Case 3.''')


# References
# 1. https://algocoding.wordpress.com/2015/04/14/how-to-sort-a-list-of-tuples-in-python-3-4/
# 2. Udacity: Data Structures & Algorithms; Data Structures; Lesson 4: Trees; 12. Code: Create a
#    Binary Tree
# 3. Udacity: Data Structures & Algorithms; Data Structures; Lesson 4: Trees; 15. Code: BST
# 4. https://medium.com/iecse-hashtag/huffman-coding-compression-basics-in-python-6653cdb4c476