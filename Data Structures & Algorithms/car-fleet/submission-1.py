class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos,s) for pos,s in zip(position,speed)]
        cars.sort(reverse=True)
        prevTime = (target-cars[0][0])/cars[0][1]
        fleets = 1
        for index in range(1,len(cars)):
            pos = cars[index][0]
            sp = cars[index][1]
            time = (target-pos)/sp
            if prevTime < time:
                fleets +=1
                prevTime = time
        return fleets
