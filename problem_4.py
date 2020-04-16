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
    
    Step 1: If it finds the name within the names list of a group,
    it returns true.
    
    Step 2: If it finds that there are no groups in its group list
    to query, it returns False.
    
    Step 3: If there are groups to continue to search for names,
    the function calls itself to keep searching.

    Commented out Print Statements: These are for debugging. Feel free to
    uncomment them for debugging.
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

# Test Case 1 Setup
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case 1 Execution, answer should be True.
print(is_user_in_group(sub_child_user, parent))

# Test Case 2
