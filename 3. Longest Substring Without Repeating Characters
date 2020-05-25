'''
Given a string, find the length of the longest substring without repeating characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:   
        a= []
        ans= 0
        for x in s:
            if x in a:
                a = a[a.index(x)+1:]
            a.append(x)    
            ans= max(ans, len(a))
        return ans
