class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_a = 0
        
        while l < r:
            h = min(height[l], height[r])
            a = h * (r-l)

            if height[r] == h:
                r -= 1
            elif height[l] == h:
                l += 1
            
            max_a = max(a, max_a)
        
        return max_a
    
# Review Attempt
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_a = 0

        while l < r:
            h = min(height[l], height[r])
            a = h * (r-l)

            if height[l] == h:
                l += 1
            else:
                r -= 1
            
            max_a = max(max_a, a)

        return max_a

