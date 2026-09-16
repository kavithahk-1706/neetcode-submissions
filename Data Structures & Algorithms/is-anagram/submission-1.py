class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        we need to track the letters that appear AND the number of times they appear
        
        """

        if len(s)!=len(t):
            return False

        s_counts=[0]*26
        t_counts=[0]*26

        for char in s:
            idx=ord(char)-ord('a')
            s_counts[idx]+=1
        
        for char in t:
            idx=ord(char)-ord('a')
            t_counts[idx]+=1
        
        return s_counts==t_counts
        
        




        
