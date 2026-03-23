#1 Leetcode 501: Find Mode in Binary Search Tree
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
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

#2 Leetcode 112: Path Sum
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)

#3 Leetcode 383: Ransom Note
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

#4 Leetcode 290: Word Pattern
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
