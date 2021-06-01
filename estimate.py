
def wallis(n):
 o=int(n)
 z=1
 pi=1
 for n in range(o):
     w=0
     w=4*z*z
     pi*=w/(w-1)
     z+=1
 return 2*pi 
 

def monte_carlo(n):
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
 

a=int(input("Enter number of iterations"))
p=wallis(a)
print(p)
q=monte_carlo(a)
print(q)
