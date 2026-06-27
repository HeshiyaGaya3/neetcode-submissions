class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        ans = ""
        for i in s:
            if i.isalnum():
                ans  += i
       
        ans = list(ans)
        rev = ans.copy()
        l = 0
        r = len(rev)-1
        while l<r:
            temp = rev[l]
            rev[l] = rev[r]
            rev[r] = temp
           
            l += 1
            r -= 1
        
            
        return ans == rev

        