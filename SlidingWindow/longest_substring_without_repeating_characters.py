class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        l = 0

        for r in range(len(s)):
            
            # if seen char found, shrink leftside
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # add new char to seen
            seen.add(s[r])

            max_len = max(max_len, len(seen))
            
        return max_len

# REDO : 7/16/2025

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time 2:09
        seen = set()
        max_len = 0

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            max_len = max(max_len, len(seen))

        return max_len