class Solution:
    def reverseVowels(self, s: str) -> str:
        # find pairs of vowels starting at the outermost ends
        s = list(s)
        i = 0
        j = len(s) - 1
        found1, found2 = False, False
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U', 'I']

        while i < j:
            if found1 and found2:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                found1, found2 = False, False
                i += 1
                j -= 1
                continue

            if s[i] not in vowels:
                found1 = False
                i += 1
            else: 
                found1 = True
            if s[j] not in vowels:
                found2 = False
                j -= 1
            else:
                found2 = True
        return "".join(s)