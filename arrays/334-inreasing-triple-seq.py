class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        find first and second smallest
        """
        first, second = float('inf'), float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            elif second < n:
                return True
        return False