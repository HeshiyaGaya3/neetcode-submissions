class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        count = 0
        temp = 0
        print(nums)
        for i in range(len(nums)-1):
            if abs(nums[i+1] - nums[i]) == 1:
                count = max(count, temp +1)
                temp += 1
            else:
                temp = 0
        if count == 0 and len(nums)==0:
            return count
     
        else:
            return count+1



        