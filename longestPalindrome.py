class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=0
        longest=""
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                substring=s[i:j]
                if substring == substring[::-1] and len(substring) > max_len:
                    max_len = len(substring)
                    longest = substring
        return longest
