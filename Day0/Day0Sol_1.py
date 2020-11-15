# Enter your code here. Read input from STDIN. Print output to STDOUT
itemCnt  = int(input())
items = list(map(int,input().strip().split()))

sumi = sum(items)
mean = round(sumi / itemCnt,1)

sortItems = sorted(items)
#print(" ".join(map(str,sortItems)))
half = itemCnt // 2
if itemCnt % 2 ==0:
    median = round(((sortItems[half-1] + sortItems[half])/2),1)
else:
    median = sortItems[half]

dicti = {}
maxCnt = 0
maxItem = int()
for item in items:
    if item not in dicti:
        dicti[item] = 1
    else:
        dicti[item] = dicti[item] + 1
    #print(str(item))
    #print(str(dicti[item]))
    if dicti[item] > maxCnt:
        maxCnt = dicti[item]
        maxItem = item
    elif dicti[item] == maxCnt:
        #print("{}  {}".format(item,maxItem))
        if item < maxItem:
            maxItem = item
#print(dicti)
print(str(mean))
print(str(median))
print(str(maxItem))

