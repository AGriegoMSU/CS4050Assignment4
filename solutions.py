'''
Problem #1 Leetcode 501: Find Mode in Binary Search Tree
    Notes:
        use stack like lecture slides
        stack filled by root
        counter to keep track of each values occurence
        max_freq to store highest occuring value
        returns value that occured most

'''
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        counter = defaultdict(int)

        while stack:
            node = stack.pop()
            counter[node.val] += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        max_freq = max(counter.values())
        return [k for k, v in counter.items() if v == max_freq]

'''
Problem #2 Leetcode 112: Path Sum
    Notes:
        Based on a tree, root
        3 cases:
            - base case, no root, returns false
            - no more branches on left or right side and target sum is achieved, returns true
            - still has more branches to evaluate, takes target and subtracts root.left or root.right 
                value until no branches remain, and target is reached, sum carried down.
        
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)
'''
Problem #3 Leetcode 383: Ransom Note
    Notes:
        Base case, if the lengths dont match, char for char match cannot either
        Counter to track available chars in magazine
        Ransom note checks chars, if none remain, returns false;
                                  if available, subtract 1 from counter[char], 
                                  continue until ransom note is complete, returns true, else false.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        counter = defaultdict(int)

        for char in magazine:
            counter[char] += 1

        for char in ransomNote:
            if counter[char] == 0:
                return False
            counter[char] -= 1

        return True

'''
Problem #4 Leetcode 290: Word Pattern
    Notes:
        split s into words, single strings that can be read
        if length of pattern and amount of words dont match, return False
        char to word -> "a" -> "dog"
        word to char -> "dog" -> "a"
        for char and word match mappings to see if patterns are same
        
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False
            if word in word_to_char and word_to_char[word] != char:
                return False
            
            char_to_word[char] = word
            word_to_char[word] = char

        return True
