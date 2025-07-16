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

        
# REDO : 7/16/2025
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time : 15:17
        nums.sort()
        # print(nums)
        res = []

        for i in range(len(nums)):
            # array is sorted, so if first index is positive, array can only get bigger, ie never be 0
            if nums[i] > 0:
                break
            # skip already seen indexes, i > 0 for index bounds
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # print(total, nums[i] , nums[l] , nums[r])

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < 0:
                    l += 1
                elif 0 < total:
                    r -= 1

        return res
                