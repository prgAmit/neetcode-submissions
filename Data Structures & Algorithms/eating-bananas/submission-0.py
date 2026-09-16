class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        MAX_PILES = max(piles)
        left, right = 1, MAX_PILES
        result = MAX_PILES

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
               hours += math.ceil(p / mid)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result