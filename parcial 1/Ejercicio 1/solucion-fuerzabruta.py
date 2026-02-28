class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        if s_sorted == t_sorted:
            return True
        else:
            return False