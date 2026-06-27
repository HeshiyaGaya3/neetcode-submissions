class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        arr = list(dic.values())
        arr.sort(reverse=True)
        arr = arr[:k]
        for key,value in dic.items():
        
            if value in arr:
                result.append(key)

        return result