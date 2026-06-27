class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        ans = []
        m = len(word1)
        n = len(word2)
        l = 0
        r = 0
        flag = 0
        while l<m and r <n:
            ans.append(word1[l])
            ans.append(word2[r])
            l += 1
            r += 1
        print(l,r)
        if l<m:
            ans += word1[l:m]
            
        if r<n:
            
            ans += word2[r:n]

        return "".join(ans)

