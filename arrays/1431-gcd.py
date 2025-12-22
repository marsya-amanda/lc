class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        merged = str1 + str2
        shorter = str1 if len(str1) <= len(str2) else str2
        shorter_len = len(shorter)
        curr_d = ""
        gcd = ""
        for i in range(shorter_len):
            curr_d += merged[i]
            if shorter_len % (i + 1) != 0: continue
            gcd = curr_d if not ''.join(merged.split(sep = curr_d)) else gcd
        return gcd

str1 = "ABCABCABC"
str2 = "ABCABC"
soln = Solution()
print(soln.gcdOfStrings(str1, str2))