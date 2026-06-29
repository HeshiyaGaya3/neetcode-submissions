class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                tot =  nums[i]+nums[l]+nums[r]
                if tot == 0 and [nums[i], nums[l], nums[r]] not in ans:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                elif tot>0:
                    r -= 1
                else:
                    l += 1
        return ans


        
        