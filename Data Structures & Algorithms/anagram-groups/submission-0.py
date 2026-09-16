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



        """

        groups_list=[]

        configs_list=defaultdict(list)

        for word in strs:
            word_count=[0]*26

            for char in word:
                word_count[ord(char)-ord('a')]+=1

            configs_list[tuple(word_count)].append(word)
            
            
        for word_list in configs_list.values():
            groups_list.append(word_list)

        return groups_list

       

        



