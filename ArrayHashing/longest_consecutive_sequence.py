class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()

        for n in nums:
            if n not in numSet:
                numSet.add(n)

        res = 0
        for n in numSet:
            if n-1 not in numSet:
                seq = n
                while seq in numSet:
                    seq += 1

                res = max(res, abs(n - seq))

        return res