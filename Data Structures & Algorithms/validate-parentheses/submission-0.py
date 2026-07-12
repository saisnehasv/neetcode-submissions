class Solution:
    def isValid(self, s: str) -> bool:
        parstack = []
        pardict = {'(':')','{':'}','[':']'}

        for i in s:
            if i in pardict:
                parstack.append(i)
            else:
                if not parstack or pardict[parstack[-1]] != i:
                    return False
                parstack.pop()
        
        return not parstack
            



        