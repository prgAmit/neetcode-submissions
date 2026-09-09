class Solution:
    def search(self, nums: List[int], target: int) -> int:           
        left = 0
        right = len(nums)-1
        return self.find_target_binary(nums, left, right, target)


    def find_target_binary(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left <0 or right <0 or left > right:
            return -1

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
            return self.find_target_binary(nums, left, right, target)
        else:
            left = mid + 1
            return self.find_target_binary(nums, left, right, target)
 