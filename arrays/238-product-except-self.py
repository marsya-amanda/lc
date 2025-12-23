def productExceptSelf(nums: list[int]) -> list[int]:
        """
        trick:
        - two for loops, one for suffix and prefix
        - dont forget to multiply both ans and nums
        """
        n = len(nums)
        suf = 1
        answer = [1 for x in nums]
        for i in range(1, n):
            answer[i] *= nums[i - 1] * answer[i - 1] # multiply with numbers on the left 
        for i in range(n - 1, -1, -1):
            answer[i] *= suf # multiply with numbers on the right
            suf *= nums[i] # not quite sure why
        
        return answer