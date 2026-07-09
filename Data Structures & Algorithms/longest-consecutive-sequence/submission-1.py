class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0 
        for i in numset:
            start = -1 
            count = 0
            if i-1 not in numset:
                start = i
                while start in numset:
                    count += 1
                    start += 1
            maxcount = max(count, maxcount)
        return maxcount

        