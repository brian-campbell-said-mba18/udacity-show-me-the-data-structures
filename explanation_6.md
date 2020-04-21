# Problem_6 Explanation

## Code Design
Finding interesections and unions are going to require iteration, there's no way to make the time complexity constant. However, this code uses dictionaries in its intersection and union functions to increase efficiency in lookups. In the intersection function, both of the linked lists are converted to their own respective unique values dictionaries. The smaller dictionary is iterated through and looks up values in the bigger dictionary in constant time using the dictionary .get() function (Reference 1). The union function starts the same way by converting the two linked lists to unique value dictionaries. Then the smaller dictionary is iterated through, doing constant lookups of its keys in the bigger dictionary. If a small key is present in the big dictionary, that key is deleted from the big dictionary. Once, the small dictionary is iterated through, the big dictionary is iterated through. However, the deleting of the intersection keys in the big dictionary adds some efficiency, so in the average case, the size of the big dictionary has been reduced once it is time to iterate through it.

## Code efficiency.
In using dictionaries in both the intersection and Union functions, both functions have a worst case O(n) time complexity. Also, both funcitons have a worst case O(n) space complexity.

## References
1. https://stackoverflow.com/questions/16926408/bigo-for-dictionary-method-getkey