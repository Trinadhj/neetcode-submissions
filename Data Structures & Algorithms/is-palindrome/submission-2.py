import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace("[^a-zA-Z0-9_]",'').lower()
        # print(s)
        s = ''.join([char.lower() for char in s if char.isalnum()])
        i , j = 0 , len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True