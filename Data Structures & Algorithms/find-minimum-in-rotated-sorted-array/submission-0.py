class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minVal = nums[0]

        while left <= right:
            if nums[left] < minVal:
                minVal = min(minVal, nums[left])
                break
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1

            minVal = min(minVal, nums[mid])
        return minVal