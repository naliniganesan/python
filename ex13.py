n=int(input())
if n>1:
   for i in range(2,3):
      if(n%i==0):
         print("yes")
      else:
         print("no")
else:
   print("no")
