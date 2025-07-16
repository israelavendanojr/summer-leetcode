class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time : 2:21
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            elif target < sum:
                r -= 1
            else:
                return [l + 1, r + 1]