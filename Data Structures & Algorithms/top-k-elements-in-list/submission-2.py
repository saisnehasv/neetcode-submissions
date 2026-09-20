class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = {}
        res = set()

        for i in nums:
            count_dict[i] = count_dict.get(i,0) + 1 
        
        sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1],reverse=True))
        return list(sorted_dict.keys())[:k]

        