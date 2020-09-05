class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = collections.Counter(s)
        st = 0
        maxst = 0
        for i, c in enumerate(s):
            if cnt[c] < k:
                maxst = max(maxst, self.longestSubstring(s[st:i], k))
                st = i + 1
        return len(s) if st == 0 else max(maxst, self.longestSubstring(s[st:], k))
