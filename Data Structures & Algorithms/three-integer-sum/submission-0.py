class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index,num in enumerate(nums):
            if num > 0:
                break
            
            if index > 0 and num == nums[index-1]:
                continue
            
            left = index + 1
            right = len(nums) - 1

            while left < right:
                threesum = num + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1 
                elif threesum <0:
                    left += 1
                else:
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
        return res

                        