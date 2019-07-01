s,n=map(int,input().split())
for i in range(s+1,n):
   if(i>1):
      for x in range(2,i):
         if(i%x==0):
            break
      else:
         print(i,end=" ")
