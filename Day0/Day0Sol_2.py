# Enter your code here. Read input from STDIN. Print output to STDOUT
itemCnt  = int(input())
X = list(map(int,input().strip().split()))
W = list(map(int,input().strip().split()))
msum = 0
wsum = 0
for ind in range(itemCnt):
    msum = msum + X[ind] * W[ind]
    wsum += W[ind]
mw = round((msum / wsum),1)
print(str(mw))

