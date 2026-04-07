class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        sortedArr = sorted(self.arr)
        arrLen = len(self.arr)
        halfArrLen = arrLen//2
        if arrLen & 1 :
            return sortedArr[halfArrLen]
        else:
            return (sortedArr[halfArrLen]+ sortedArr[halfArrLen-1])/2
        
        