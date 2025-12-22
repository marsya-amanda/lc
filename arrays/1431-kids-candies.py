class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        old_max = max(candies)
        for i, candy in enumerate(candies):
            # note: use enumerate, CANDY IS A COPY OF CANDIES[i]
            candies[i] = True if candy + extraCandies >= old_max else False
        return candies