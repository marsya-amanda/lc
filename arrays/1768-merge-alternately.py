class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return self.mergeAlternately1(word1, word2) if len(word1)>=len(word2) else self.mergeAlternately2(word1, word2)
    
    def mergeAlternately1(self, word1, word2):
        # longer word1
        merged = ""
        for i2, l2 in enumerate(word2):
            merged += word1[i2] + word2[i2]
        add = int(len(merged) / 2)
        print(add)
        return merged + word1[add:]
    
    def mergeAlternately2(self, word1, word2):
        # longer word1
        merged = ""
        for i1, l1 in enumerate(word1):
            merged += word1[i1] + word2[i1]
        add = int(len(merged) / 2)
        return merged + word2[add:]

soln = Solution()
soln2 = soln.mergeAlternately("abc", "pqr")
print(soln2)