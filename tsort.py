
t = int(input())
nList = [0]*t
for i in range(t):
    nList[i] = int(input())
sortedList = sorted(nList)
for n in sortedList:
    print n