class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        i = 0
        mid = len(words) // 2 # when finding mid point, do floor div
        while i < mid:
            temp = words[i]
            words[i] = words[-i - 1]
            words[-i - 1] = temp
            i += 1

        return " ".join(words)