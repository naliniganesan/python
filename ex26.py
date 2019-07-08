u1 = int(input())
v1 = list(map(int,input().split()))
v1.sort()
for i in range(u1):
  print(v1[i],end=" ")
