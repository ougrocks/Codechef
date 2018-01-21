
N=int(input().strip())
n1=0
n2=0
a=0
win=0
while(N>0):
    x,y=[int(i) for i in input().split()]
    n1+=x
    n2+=y
    if(n1>=n2):
        b=n1-n2
    else:
        b=n2-n1
    if(a<b and n1>n2):
        win=1
        a=b
    elif(a<b and n1<=n2):
        win=2
        a=b
    N-=1
print(str(win)+" "+str(a))