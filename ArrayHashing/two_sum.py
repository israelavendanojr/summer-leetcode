class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in hash:
                return [i, hash[needed]]
            
            hash[nums[i]] = i

        return []

# REDO : 7/15/2025

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TIME : 2:51
        hash = {}

        for i in range(len(nums)):
            desired = target - nums[i]

            if desired in hash:
                return [i, hash[desired]]
            else:
                hash[nums[i]] = i

        return []
            