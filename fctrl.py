nMin = 1
nMax = 1000000000


def z(n):
    zerosCount = 0
    divideN = 5
    while (divideN <= n):
        zerosCount += n // divideN
        divideN *= 5
    return zerosCount


t = int(input())
nList = [0] * t
for i in range(t):
    n = int(input())
    if (n >= nMin and n <= nMax):
        nList[i] = z(n)
for zeros in nList:
    print(zeros)