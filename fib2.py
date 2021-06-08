def c(a):
 if (a==0):
   return 0
 elif (a==1):
   return 1
 return c(a-1)+c(a-2)


d=int(input("podaj dlugosc ciagu "))
x=0
for x in range (d):
   x=x+1
   print(c(x))