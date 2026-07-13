class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp = []
        
        for index,temperature in enumerate(temperatures):
            while temp and temperature > temp[-1][0]:
                t,i = temp.pop()
                result[i] = index-i
            temp.append((temperature,index))
        
        return result
        


        