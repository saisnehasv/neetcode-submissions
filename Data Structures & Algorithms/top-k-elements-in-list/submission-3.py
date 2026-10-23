class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i,0) + 1

        count_dict = dict(sorted(count_dict.items(),key = lambda item: item[1],reverse = True))
        return list(count_dict)[:k]
        