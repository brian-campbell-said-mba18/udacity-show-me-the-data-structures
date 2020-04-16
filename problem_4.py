class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    
    This recursive search has three steps.
    
    Step 1: if it finds the name within the names list of a group,
    it returns true.
    
    Step 2: if it finds that there are no groups in its group list
    to query, it returns False.
    
    Step 3: If there are groups to continue to search for names,
    the function calls itself to keep searching.

    Commented out Print Statements: These are for debugging. Feel free to
    uncomment them for debugging.

    Note on References: See References at the end of the script. I borrowed the idea
    to use a for loop to activate a recursive function from Reference 1.
    """
    
    # This is step 1
    if user in group.get_users():
        # print("Found: {} in group: {}. True. BREAK!!!!".format(user, group.get_name()))
        return True
    
    # This is step 2
    if len(group.get_groups()) == 0:
        # print("Group: {} has no group list. False.\n".format(group.get_name()))
        return False
    
    # This is step 3
    # print("Going deeper into the matrix, Group: {} has groups...\n".format(group.get_name()))
    group_list = group.get_groups()
    for i in group_list:
        output = is_user_in_group(user, i)
        if output:
            break
        
    return output

# Test Case 1 Setup. This is the given
# test from Udacity.
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case 1 Execution: the answer should be True.
print(is_user_in_group(sub_child_user, parent))

# Test Case 2 Setup: it is the Same as Test Case 1,
# but the user == None.
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = None
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case 2 Execution: the answer should be True.
print(is_user_in_group(sub_child_user, parent))

# Test Case 3 Setup: I make the Group structure larger,
# and the user is an integer value.
parent = Group("parent")

child = Group("child")
silly_child = Group("silly child")

sub_child = Group("subchild")
sub_silly_child = Group("sub silly child")

strange_integer_value = 42
sub_child_user = "sub child user"

sub_child.add_user(sub_child_user)
sub_silly_child.add_user(strange_integer_value)

child.add_group(sub_child)
silly_child.add_group(sub_silly_child)

parent.add_group(silly_child)
parent.add_group(child)

# Test Case 3 Execution: the answer should be True.
print(is_user_in_group(strange_integer_value, parent))

# References
# 1. https://github.com/rahulatrkm/Show-Me-the-Data-Structures./blob/master/solution_2.py