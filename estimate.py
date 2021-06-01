def wallis(n):
 import random
 incircle=0
 outcircle=0
 o=int(n)
 for n in range(o):
  x=random.random()
  y=random.random()
  if (((x**2+y**2)**0.5)>1) :
    outcircle+=1
  else:
    incircle+=1
 pi=4*(incircle/(outcircle+incircle))
 return pi

m=input()
p=wallis(m)
print("The estimated value of pi is",p)
