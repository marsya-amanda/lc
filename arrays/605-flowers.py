class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        zero_count = 0
        at_zero = True
        flowerbed[0:0] = [1, 0]
        flowerbed.extend([0, 1]) # cannot use splicing if at end
        planted = 0

        for f in flowerbed:
            if f == 1:
                planted += (zero_count - 1) // 2 if zero_count > 2 else 0
                zero_count = 0
            elif f == 0:
                zero_count += 1
        return planted >= n
    
soln = Solution()
soln.canPlaceFlowers([1, 0, 1, 0, 1], 1)