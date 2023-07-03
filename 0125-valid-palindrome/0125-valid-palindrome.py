class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.sub(r"[^\uAC00-\uD7A3a-zA-Z0-9]", "", s)

        for i in range(len(s)//2):
            if s[i] != s[-1 - i]:
                return False
        return True
