class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #track whether a number has been seen before?
        #keep a flag to track

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False