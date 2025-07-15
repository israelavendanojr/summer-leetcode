class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True

        return False

# REDO : 7/15/2025
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TIME : 0:41
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)

        return False