class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] * nums[i]

        # suffix sum

        suffixSum = [0] * n
        suffixSum[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] * nums[i]
        
        # print(prefixSum, suffixSum)
        # make res
        res = [0] * n
        res[0] = 1 * suffixSum[1]
        res[-1] = prefixSum[-1 - 1] * 1
        for i in range(1,len(nums)-1):
            res[i] = prefixSum[i-1] * suffixSum[i+1]

        return res
    

        
        

        