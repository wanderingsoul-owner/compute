# C:12.01  H:1.008  O:16.00  N:14.01
date=int(input())
dates=[]
for i in range(date):
    m=0         #起始重量等于0
    ch=input()
    for x in ch:
        if x=="C":
            e=12.01
            m+=e
        elif x=="H":
            e=1.008
            m+=e
        elif x=="O":
            e=16.00
            m+=e
        elif x=="N":
            e=14.01
            m+=e
        else:
            t=int(x)
            m+=((t-1)*e)
    M='%.3f' % m
    dates.append(M)
for y in dates:
    print(y)