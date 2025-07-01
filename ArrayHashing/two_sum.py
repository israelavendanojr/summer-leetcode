class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in hash:
                return [i, hash[needed]]
            
            hash[nums[i]] = i

        return []
            