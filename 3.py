l=input()
v=['a','e','i','o','u','A','E','I','O','U']
c=['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','B','V','N','M']
if l in v:
   print("Vowel")
elif l in c:
   print("Consonant")
else:
   print("invalid")
