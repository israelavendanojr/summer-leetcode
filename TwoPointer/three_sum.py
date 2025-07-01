class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                val = nums[i] + nums[l] + nums[r]

                if val < 0:
                    l += 1
                elif 0 < val:
                    r -= 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    res.append(triplet)

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    
        return res

        