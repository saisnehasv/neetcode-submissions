class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        for i in s :
            count_s[i] = count_s.get(i,0) + 1;
        
        for j in t:
            if j not in count_s:
                return False

            else:
                count_s[j] -= 1
                if count_s[j] == 0:
                    del count_s[j]
        return len(count_s) == 0