class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        if s_count == t_count:
            return True

        return False

# REDO : 7/15/2025

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time : 1:15
        s_count = Counter(s)
        t_count = Counter(t)

        if s_count == t_count:
            return True
        else:
            return False