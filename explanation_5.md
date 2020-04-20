# Problem_5 Explanation

## Code Design
I used the required data structures, a node class called Block() with init variables of self.timestamp, self.data, self.hash, self.previous, and self.next, and a linked list class called Block_Links. Block_Links only has the ability to add blocks. I contemplated having a delete function, but I thought that since deleting a block in a block chain is a complicated process, it'd be best to leave that function out (Reference 1). 

## Code efficiency.
In the worst case, when Block_Links.append() is called, it has a O(1) time complexity, but the space complexity is O(n). Essentially, the space complexity depends upon the number of times Block_Links.append() has been called previously. Something to note about Block_Links.append() is that every time a unique hash is added to the Block_Links structure, that hash code is added to a hash dictionary repository. Also, every time a new block is about to be added when the Block.append() function is called, the hash dictionary is checked to ensure that the hash string to be converted to a hash code is a unique hash string. If not, an error arises, and the block is not added. Even in using the .get() function to check the hash dictionary to ensure that the hash string to be encoded is unique, using the Block_Links.append() method takes O(1) time (Reference 2). Finally, printing the Block_Links() structure with print(Block_Links()) takes, in the worst case, O(n) time, because printing each block depends upon how many times the Block_Links.append() function was called. However, the print function does not actually store anything, so the worst case space complexity for the print function is O(0).

## References
1. https://en.wikipedia.org/wiki/Blockchain
2. https://stackoverflow.com/questions/16926408/bigo-for-dictionary-method-getkey