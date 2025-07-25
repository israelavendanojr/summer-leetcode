class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        cur_sum = 0

        # iterate first window of k elements
        for i in range(k):
            cur_sum += nums[i]

        max_sum = max(max_sum, cur_sum)

        # sliding window, remove i+k and add i to move window sum
        for i in range(k, len(nums)):
            cur_sum -= nums[i-k]
            cur_sum += nums[i]

            max_sum = max(max_sum, cur_sum)


        return max_sum / k
            

# REDO : 7/16/2025

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time : 2:01
        max_sum = float('-inf')
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]

        max_sum = max(max_sum, cur_sum)
        

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]

            max_sum = max(max_sum, cur_sum)

        return max_sum / k