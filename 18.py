s,e=[int(x) for x in input().split()]
for n1 in range(s,e+1):
   o=len(str(n1))
   s=0
   t1=n1
   while t1>0:
      digit=t1%10
      s += digit**o
      t1//=10
   if n1==s:
      print(n1,e=" ")
