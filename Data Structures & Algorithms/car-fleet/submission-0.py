class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(pos,s) for pos,s in zip(position,speed)]
        cars.sort(reverse=True)
        for pos,sp in cars:
            time = (target-pos)/sp
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
