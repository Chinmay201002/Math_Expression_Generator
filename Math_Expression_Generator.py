import random as r
import time as t

operators=["+","-","*","%"]
min_value=1
max_value=15
total_problems=10

def generate():
  left=r.randint(min_value,max_value)
  mid=r.choice(operators)
  right=r.randint(min_value,max_value)

  expr=str(left)+" "+mid+" "+str(right)
  ans=eval(expr)

  return expr,ans

print("Press enter to Start")
print("----------------------------------------------")

start_time=t.time()

for i in range(total_problems):
  exp,answer=generate()
  while True:
    print("Problem #"+str(i+1))
    solve=int(input(exp+"="))
    if(solve==answer):
      break


end_time=t.time()

total_time=round(end_time-start_time,2)

print("----------------------------------------------")
print("Excellent Work")

print("You have completed all"+" "+str(total_problems) +" problems in just",total_time," "+"seconds")