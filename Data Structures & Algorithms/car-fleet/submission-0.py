class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse = True)
        carfleet = []
        
        for p,s in pairs:
            carfleet.append((target - p) / s)
            if len(carfleet) >= 2 and carfleet[-1] <= carfleet[-2]:
                carfleet.pop()

        return len(carfleet)




        