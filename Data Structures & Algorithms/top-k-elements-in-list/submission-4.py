class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        freqdict = {}
        res = []
        for i in nums:
            count_dict[i] = count_dict.get(i,0) + 1
        for key,value in count_dict.items():
            if value in freqdict:
                freqdict[value].append(key)
            else:
                freqdict[value] = [key]
        
        for j in range(len(nums),0,-1):
            if j in freqdict:
                res.extend(freqdict[j])
                k -= len(freqdict[j])
                if k == 0:
                    break
        
        return res


        # count_dict = dict(sorted(count_dict.items(),key = lambda item: item[1],reverse = True))
        # return list(count_dict)[:k]