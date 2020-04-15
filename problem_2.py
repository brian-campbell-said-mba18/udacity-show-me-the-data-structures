import os

def find_files(path, the_end):
    """
    Find all files beneath path with file ending in,
    the_end, the specified file end string variable.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

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
        This function either appends the path of a file that ends
        with the specified the_end variable from the find_file
        function, investigates a directory recursively, or passes
        over a file.

        Note on print statements: The commented out print statements
        were used for debugging. These can be uncommented to see what
        happens in this function.
        """
        new_path = var_path + "/" + some_item

        # This appends the path of a file that ends with
        # the specified ending, the_end.
        if some_item.endswith(the_end):
            list_of_paths.append(new_path)
            #print("FOUNDS SOMETHING!!!!")
            #print("Appended {}".format(some_item))
            #print("______________________________\n")

        # This explores another directory and calls up
        # the_recursive. If this condition is not met, then 
        # this is the last of the if statements and nothing happens.
        if os.path.isdir(new_path):
            #print("Exploring new path {}...".format(new_path))
            #print("______________________________\n")
            for i in os.listdir(new_path):
                the_recursive(i, new_path)
    
    # This starts the for loop, creates a list of files and
    # directories to explore in the overaching path, and
    # calls the_recursive function.
    for item in os.listdir(path):
        the_recursive(item, path)

    # This list of paths is returned as output.
    return list_of_paths

print(find_files('testdir', ".c"), '\n')
print(find_files("scavenger-hunt-1", ".docx"), '\n')
print(find_files("scavenger-hunt-2", ".txt"))

# References
# 1. https://github.com/rahulatrkm/Show-Me-the-Data-Structures./blob/master/solution_2.py