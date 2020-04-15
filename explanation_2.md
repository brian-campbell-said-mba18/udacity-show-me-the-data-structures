# Problem_2 Explanation

## Code Design
I used the lists created by the functions in the OS modules. I used these lists for convenience, it didn't make
much sense to create my own function to store paths in a data strucutre. Also, I used lists because every single path needed to be iterated through, and lists are good structures for iteration.

## Efficiency
The worst-case big O time complexity calculation is O(n^2); there are for loops embedded in for loops in the function. The worst-case space complexity is also O(n^2); if every single item iterated through the embedded for loops were stored it owuld take O(n^2) space.