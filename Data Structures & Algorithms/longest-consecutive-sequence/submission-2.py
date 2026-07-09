class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0 
        for i in numset:
            count = 0
            if i-1 not in numset:
                length = 1
                while length + i in numset:
                    length += 1
                maxcount = max(length, maxcount)
        return maxcount

        