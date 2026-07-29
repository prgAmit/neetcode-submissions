class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        set_nums = set(numbers)

        for i, n in enumerate(numbers):
            diff = target - n

            if diff in set_nums:
                j = numbers.index(diff)
                if i != j:
                    return [i+1, j+1]