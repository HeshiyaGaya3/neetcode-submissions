class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        ans = []
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
            if hm[i] > len(nums)//3 and i not in ans:
                
                ans.append(i)
        return ans
