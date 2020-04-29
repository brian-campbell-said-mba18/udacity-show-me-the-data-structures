# Problem_3 Explanation

## Code Design
To find the counts for each character, I used a dictionary that recorded unique characters and their counts. I then converted the dictionary to a list of tuples of (counts, unique character). Each tuple become a node that was inserted into custom data structure called a Priority_Stack class. This class allowed me to store nodes in ascending order: the nodes with the smallest frequencies at the top of the stack, and the nodes with the greatest at the bottom. The priority stack allowed me to create my frequency tree. I then used a recursive function to iterate through all the nodes and assign them huffman codes.

## Efficiency
The worst-case big O time complexity calculation is O(n^2), where n is the number of characters in the string. When the tuples are added to the Priority_Stack class, each tuple is iterated through and a while loop is activated to ensure the order of the stack. This part of the big O equation has the most computational steps. The while loop makes the additional number of steps taken not constant, but rather exponential. On the other hand, the big O space calculation is better than the time calculation. While each character is stored and iterated through, each iteration takes up less space than the original character, making the worst case big O calculation O(log(n)).