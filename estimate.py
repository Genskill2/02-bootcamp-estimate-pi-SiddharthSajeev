def wallis(n):
 import random
 incircle=0
 outcircle=0
 for n in range(n):
  x=random.random()
  y=random.random()
  if(x>y):
       if(y>=((1-x**2)**0.5)):
        incircle+=1
       else:
        outcircle+=1
  elif(y>x):
       if(y>=((1-x**2)**0.5)):
        incircle+=1
       else:
        outcircle+=1
  elif(x==y): 
       if(x>(1/(2**0.5))):
        outcircle+=1
       else:
        incircle+=1
 pi=16*(incircle/(outcircle+incircle))
 print("The estimated value of pi is",pi);
wallis(50000);
