#1.1 Implement a recursive function to calculate the factorial of a given number.

def fact(x):
  if x==1:
    return 1
  else:
    print(x)
    sum=x*fact(x-1)
    return (sum)
num=int(input("enter a number:"))
if num>=-1:
    print("factorial value",fact(num))