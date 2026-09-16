from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        what should we do?
        given a list of strings,
        return a list of list of strings
        each list should consist of its own set of anagrams

        keep track of each word seen (through original list),
        check counts configuration,
        and see if for each such word there are any matches in the rest

        so each word has its own configuration of letters and counts

        do we store each and compare pairwise? that's inefficient- probably brute force

        imp notes:
        

        1. defaultdict is your friend if you want to append to values of keys without having to specify the initial values themselves
        2. the key needs to be the unique/singular/shared thing while the value needs to be the thing associateed with that thing, not the other way round. me trying to compare the keys for their respective values was where it was going wonky bc how much are you gonna do pairwise key comparison 
        making the key independently computable per item with no need for comparison is important.
        if two words produce the identical signature, they're automatically bucketed together with zero comparisons ever happening.

        """

        groups_list=[]

        configs_list=defaultdict(list)

        for word in strs:
            word_count=[0]*26

            for char in word:
                word_count[ord(char)-ord('a')]+=1

            configs_list[tuple(word_count)].append(word)
            
            
        return list(configs_list.values())

       

        



