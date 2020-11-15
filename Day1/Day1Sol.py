# Enter your code here. Read input from STDIN. Print output to STDOUT
itemCnt  = int(input())
elements = list(map(int,input().strip().split()))
frequency = list(map(int,input().strip().split()))

def findMedian(theList,startInd,endInd):
    itemCnt  = endInd - startInd + 1
    even = True
    median = -1
    index1 = -1
    index2 = -1
    if itemCnt % 2 != 0:
        even=False
    if even:
        index1 = (itemCnt//2) - 1 + startInd
        index2 = (itemCnt//2) + startInd
        median = (theList[index1] + theList[index2] ) / 2
    elif not even:
        half = itemCnt // 2 + startInd
        index1 = half - 1
        index2 = half + 1
        median = theList[half]
    return median,startInd,index1,index2,endInd

S = []

for ind in range(itemCnt):
    for i in range(frequency[ind]):
        S.append(elements[ind])
S.sort()
#print(S)
sLen = len(S)
Q2, Q1Start, Q1End, Q3Start,Q3End = findMedian(S,0,sLen-1)
#print("{} {} {} {}".format(str(Q1Start), str(Q1End), str(Q3Start),str(Q3End)))
Q1,a,b,c,d = findMedian(S,Q1Start,Q1End)
#print("{} {} {} {}".format(str(a), str(b), str(c),str(d)))
Q3,a,b,c,d = findMedian(S,Q3Start,Q3End)
#print("{} {} {} {}".format(str(a), str(b), str(c),str(d)))
diff = round((Q3 - Q1)/1, 1)
print(str(diff))