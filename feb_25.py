# # def example(a,b):
# #     print("example function is working")
# #     print(a,b)
# #     return a,b

# # a,b=example("a","b")

# # arguments, parameters

# # 1) normal function
# # 2) parameterized functions
# # 3)default parameterized functions
# # 4)keyword arguments
# # 5) args 
# # 6)kwargs

# # def example(a=0,b=0):
# #     return a+b

# # print(example())

# # def example(first,second,third):
# #     return first+second+third

# # print(example(secon="techno",first="royal",third="pvt ltd"))


# # arbitary arguments
# # *

# # def exampt(b,a)
# #     c=list(b)
# #     for i in range(len(c)):
# #         if c[i] == 3:
# #             c[i] = 33
# #             break
# #     return tuple(c)
# # print(example(1,2,3,4,5,6,7,8,9,1le(a,*b):
#     # prin0))

# # kwargs
# # keyword arbitary args

# # def examlpe(**c):
# #     print(c)
# # examlpe(apple="red")

# # Real Python Is Great !
# 'RealPythonIsGreat!'

# # def example(**data):
# #     # pass
# #     print(data)
# #     str1=""
# #     # for i in data.values():
# #     #     str1+=i
# #     return str1.join(data.values())

# # print(example(a="Real",b="Python",c="Is",d="Great",e="!"))


# # decorators

# # function in function
# # def check1(func):
# #     def inner(a,b):
# #         print("in decorator")
# #         if a > 0 and b > 0:
# #             func(a,b)

# #     return inner

# # @check1
# # def mul1(a,b):
# #     print("in sum")
# #     print(a*b)

# # mul1(1,2)


# def make_pretty(func):

#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()  




# def factorial_decorator(func):
#     def inner(n):
#         if n < 0:
#             return 1
#         elif n == 0 or n == 1:
#             return 1
#         else:
#             return func(n)
#     return inner

# @factorial_decorator
# def calculate_factorial(n):
#     return n * calculate_factorial(n - 1)

# # Test the decorated function

# print(calculate_factorial(5))
# # print(f"Factorial: {result}")




# def check1(func):
#     def inner(a,b):
#         print("in decorator")
#         if a > 0 and b > 0:
#             print(func(a,b))
#     return inner

# @check1
# def sum1(a,b):

#     print("in sum")
#     return a*b

# sum1(1,2)

# # # def make_pretty(func):

# # #     def inner():
# # #         print("I got decorated")
# # #         func()
# # #     return inner

# # # @make_pretty
# # # def ordinary():
# #     # print("I am ordinary")

# # # ordinary()  



# # def factorial_decorator(func):
# #     def inner(n):
# #         if n < 0:
# #             return 1
# #         elif n == 0 or n == 1:
# #             return 1
# #         else:
# #             return func(n)
# #     return inner

# # @factorial_decorator
# # def calculate_factorial(n):
# #     return n * calculate_factorial(n - 1)

# # # Test the decorated function

# # result = calculate_factorial(4)
# # print(f"Factorial: {result}")


# marks =[56,78,90,100,50]
# get_ave(marks)