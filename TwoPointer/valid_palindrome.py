class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

# REDO : 7/16/2025
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time 04:28
        pal = ''

        # preprocess input
        for c in s:
            if c.isalnum():
                pal += c.lower()

        # palindrome Check
        l, r = 0, len(pal)-1
        while l < r:
            if pal[l] == pal[r]:
                l += 1
                r -= 1
            else:
                return False

        return True