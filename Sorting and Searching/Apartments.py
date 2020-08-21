def v():return map(int,input().split())
n,m,k=v()
a,b,c,j,i=sorted(v()),sorted(v()),0,0,0
while i<n and j<m:
    if a[i]+k<b[j]:
        i+=1
    elif a[i]-k>b[j]:
        j+=1
    else:
        c+=1
        j+=1
        i+=1
print(c)