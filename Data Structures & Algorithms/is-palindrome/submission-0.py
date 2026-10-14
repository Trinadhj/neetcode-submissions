import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r"[A-z0-9]",s))
        s = s.lower()
        i,j = 0, len(s)-1
        while i <= j:
            if ord(s[i]) != ord(s[j]):
                return False
            i += 1
            j -= 1
        return True