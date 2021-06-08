n=input("podaj liczbe ")
n=int(n)
a, b = 0, 1
for i in range(n):
   i=a + b
   a=b
   b=i
   print(i)