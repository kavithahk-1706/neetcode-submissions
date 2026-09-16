class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        we need to track the letters that appear AND the number of times they appear
        solution: HASHMAP
        """
        s_chars={char:0 for char in s}
        t_chars={char:0 for char in t}

        for char in s:
            s_chars[char]+=1
        for char in t:
            t_chars[char]+=1
        
        if s_chars==t_chars:
            return True

        return False
