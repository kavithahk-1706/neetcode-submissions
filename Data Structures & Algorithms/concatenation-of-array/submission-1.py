class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # for length n, create an array of length 2n
        ans=[]
        for i in range(2):
            ans.extend(nums)

        return ans

            