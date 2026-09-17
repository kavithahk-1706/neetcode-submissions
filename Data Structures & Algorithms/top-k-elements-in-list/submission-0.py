
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        keep track of numbers, aND the frequency of occurrence

        hash map??
        """
        output=[]
        counts=defaultdict(int)
        heap=[]
        for num in nums:
            counts[num]+=1
        
        for num, freq in counts.items():
            heapq.heappush(heap,(-freq, num))
        
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output
            
        

    

        
