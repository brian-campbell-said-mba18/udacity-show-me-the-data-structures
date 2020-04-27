# Problem_4 Explanation

## Code Design
Names are stored in lists, which means that the lists must be iterated through in order for a queried name to be found. Since there was no way to escape iteration, I created a function that first looked in a list of names, then checked the length of the group list, and then activated a for loop that recursively searched for the name for each group in the group list. However, the function returns True and breaks once the name is found, so in the average case, when the name is in the data structure, it does not have to iterate through the entire structure.

## Code efficiency.
In the worst case, this code has a O(n^2) time efficiency because of the for loops embedded in for loops, where n is defined as all the groups in the data structure. The function returns either True or False, giving it a worst case space efficiency calculation of O(1).