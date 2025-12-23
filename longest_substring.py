class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char={}
        length=0
        left=0
        for index,right in enumerate(s):
            if right in char and char[right]>=left:
                left=char[right]+1
            char[right]=index
            length=max(length,index-left+1)
        return length
