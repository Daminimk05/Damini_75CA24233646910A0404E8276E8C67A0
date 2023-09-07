#Program to find the factorial of a number using recursion

def fact_recur(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_recur(n-1)

#Getting input from the user:
num= int(input("Enter a number:"))
print("The factorial of",num, "is" ,fact_recur(num))
