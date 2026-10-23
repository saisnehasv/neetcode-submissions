class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        freq = [[] for i in range(len(nums)+1)]
        res= []
        for i in nums:
            count_dict[i] = count_dict.get(i,0) + 1
        
        for num, count in count_dict.items():
            freq[count].append(num)
        
        for j in range(len(nums),0,-1):
                res.extend(freq[j])
        
        if len(res) >= k:
            return res[:k]
        
        return res
        