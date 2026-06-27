class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # Step 1: create output array filled with 1
        output = [1] * n
        
        # Step 2: fill left products
        left = 1
        for i in range(n):
            output[i] = left
            left = left * nums[i]
        
        # Step 3: multiply with right products
        right = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * right
            right = right * nums[i]
    
        return output
