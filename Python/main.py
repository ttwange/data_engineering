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

# def fact(x):
#   c = 1

#   for i in range(1, x+1):
#     c *= i
#     yield c

# for z in fact(3):
#   print(z)

#recussion is a function calling itself

# def fact(n):
#   if (n==0 or n==1):
#     return 1
#   else:
#     return n*fact(n-1)
  
# result = fact(5)

# print(result)


# for x in range(1,5):
#   a = lambda x: x ** 2
#   print(a(x))

# y = [1,2,3,4,5,6,7,8,9]

# b = map(lambda x: x ** 2,y)
# print(list(b))

# c = list(filter(lambda x: x % 2 == 0, y))

# print(c)

# from functools import reduce

# d = reduce(lambda x,y : x+[y ** 2],y,[])
# print(list(d))

# def funct(fun):
#   def wrapper(*args, **kwargs):   
#     print("calling before the fun")
#     result = fun(*args, **kwargs)
#     print("Calling after the fun")
#     return result
#   return wrapper


# @funct
# def my_sum(a,b):
#   return a + b

# result = my_sum(1,2)
# print(result)

class Computer:

  def __init__(self, ram, cpu):
    self.cpu  = cpu
    self.ram = ram

  def config(self):
    print(" Config is", self.cpu, self.ram)

com1 = Computer("i7",16)

#com1.config()



com1.config()

