u = int(input())
v = list(map(int,input().split()))
v.sort()
for i in range(u):
  print(v[i],end=" ")
