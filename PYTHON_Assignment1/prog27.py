#Python program to find the Nth term in a Fibonacci series using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0  
   elif n == 1:
        return 1  
      else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input(" enter the value of n:"))
if n<0:
  print("please enter a positive integer.")
  else:
       result = fibonacci_recursive(n)
        print(f"The {n}-th Fibonacci number is: {result}")
