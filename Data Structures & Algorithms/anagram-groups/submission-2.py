class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            if  "".join(sorted(i)) not in anagram:
                anagram["".join(sorted(i))] = [i]
            else:
                anagram["".join(sorted(i))].append(i)
            
        return list(anagram.values())
               

        