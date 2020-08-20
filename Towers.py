from bisect import bisect_right
l,t,n,z=[],0,int(input()),[int(i)for i in input().split()]
for i in z:
    p=bisect_right(l,i)
    if p>=t:
        l+=[i]
        t+=1
    else:
        l[p]=i
print(t)
