class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={num:0 for num in nums}
        for num in nums:
            seen[num]+=1
        for num in seen:
            if seen[num]>1:
                return True
        return False