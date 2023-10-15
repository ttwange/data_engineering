# def fib(n):
#   a = 0
#   b = 1
#   if n < 0:
#     print("Incorrect input")
#   elif n == 1:
#     print(a)
#   else:
#     for i in range(2,n):
#       c = a+b
#       a=b
#       b=c
#       print(c)

# fib(100)

def fact(x):
  c = 1

  for i in range(1, x+1):
    c *= i
    yield c

for z in fact(3):
  print(z)
