class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for i in s:
            count[i] = count.get(i,0) + 1
        
        for j in t:
            if j in count:
                count[j] -= 1
                if count[j] == 0:
                    del count[j]
            else:
                return False
        
        return len(count) == 0
            