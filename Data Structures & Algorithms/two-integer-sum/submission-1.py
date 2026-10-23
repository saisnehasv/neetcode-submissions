class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
         
        for i,n in enumerate(nums):
            n2 = target - n
            if n2 in count:
                return [count.get(n2),i]
            else:
                count[n] = i