class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        contador = {}
        for letra in s:
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    
        for letra in t:
            if letra in contador:
                contador[letra] -= 1
            else:
                return False
        
        for valor in contador.values():
            if valor != 0:
                return False
        
        return True