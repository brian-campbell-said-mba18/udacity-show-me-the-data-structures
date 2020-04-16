import os

def find_files(path, the_end):
    """
    Find all files beneath path with file ending in, the_end, the specified file end string variable.

    Note that a path may contain further subdirectories and those subdirectories may also contain
    further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      the_end(str): the file to return if the file has this specified ending.
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_paths = []

    assert os.listdir(path), "Unable to find the path. Please try resetting the CWD!"

    # This creates the recursive function within the function.
    def the_recursive(some_item, var_path):
        """
        This function either appends the path of a file that ends with the specified
        the_end variable from the find_file function, investigates a directory
        recursively, or passes over a file.

        Note on print statements: The commented out print statements were used for debugging. 
        These can be uncommented to see what happens in this function.
        """
        new_path = var_path + "/" + some_item

        # This appends the path of a file that ends with the specified ending, the_end.
        if some_item.endswith(the_end):
            list_of_paths.append(new_path)
            #print("FOUNDS SOMETHING!!!!")
            #print("Appended {}".format(some_item))
            #print("______________________________\n")

        # This explores another directory and calls up the_recursive. If this condition is
        # not met, then this is the last of the if statements and nothing happens.
        if os.path.isdir(new_path):
            #print("Exploring new path {}...".format(new_path))
            #print("______________________________\n")
            for i in os.listdir(new_path):
                the_recursive(i, new_path)
    
    # This starts the for loop, creates a list of files and directories to explore in the
    # overaching path, and calls the_recursive function.
    for item in os.listdir(path):
        the_recursive(item, path)

    # If there is nothing in the list, the function returns none.
    if len(list_of_paths) == 0:
        return None

    # This returns the list of paths, given that there is something in the list.
    return list_of_paths

# This is Test Case 1, given by Udacity.
print("Test Case 1 results:")
print(find_files('testdir', ".c"), '\n') # Several files should be returned.

# This is Test Case 2.
print("Test Case 2 results:")
print(find_files("scavenger-hunt-1", ".docx"), '\n') # Several files should be returned.

# This is Test Case 3.
print("Test Case 3 results:")
print(find_files("scavenger-hunt-2", ".txt"), '\n') # Several files should be returned.

# This is Test Case 4.
print("Test Case 4 results:")
print(find_files("scavenger-hunt-2", ".pdf"), '\n') # None should be returned. There are no PDFs under this directory.

# References
# 1. https://github.com/rahulatrkm/Show-Me-the-Data-Structures./blob/master/solution_2.py