n=int(input())
j=list(map(int,input().split()))
print(sum(j) if sum(j)-max(j)>=max(j) else max(j)*2)