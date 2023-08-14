class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
            left = 0
            total = sum(nums)
            
            for i, value in enumerate(nums):
                if left == total - left - value:
                    return i
                left += value
            return -1




