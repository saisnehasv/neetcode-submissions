class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        valid_k = 0
        while left <= right:
            k = left + (right - left)//2
            hours = 0 
            for p in piles:
                hours += math.ceil(float(p)/k)
            if hours <= h :
                res = k 
                right = k - 1
            else:
                left = k + 1
        
        return res
            

            
        