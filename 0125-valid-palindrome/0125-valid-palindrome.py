class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.sub(r"[^\uAC00-\uD7A3a-zA-Z0-9]", "", s)
        s_reverse = s[::-1]
        return s == s_reverse
