class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict={}
        for letter in s:
            if letter not in dict:
                dict[letter]=1
            else:
                dict[letter]+=1
        
        for letter in t:
            if letter not in dict:
                return False
            else:
                dict[letter]-=1
                
        for value in dict.values():
            if value!=0:
                return False
        return True 