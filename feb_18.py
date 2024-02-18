# 

# def club_example():
#     # print("hello function") 
#     return "hello function"

# x=club_example()
# print(x)

# parameters vs arguments
def example(a,b):
    print("example function is working")
    # print(a,b)
    return a,b

a,b=example("a","b")

list1=['12','33','44','66'] 
tuple1=('66','77','88','99')

# create a function that takes list1 and tuple1 as arguments,
# convert each element from both into interger 
# and return the updated list and tuple
# def convert(list1,tuple1):
#     l1=[]
#     l2=[]
#     for i in list1:
#         l1.append(int(i))
#     for j in tuple1:
#         l2.append(int(j))
#     return l1,tuple(l2)
# print(list1)
# print(tuple1)
# l,t=convert(list1,tuple1)
# print(l)
# print(t)
# arguments, parameters

# 1) normal function
# 2) parameterized functions
# 3)default parameterized functions
# 4)keyword arguments
# 5) args 
# 6)kwargs

# def example(a=0,b=0):
#     return a+b

# print(example(5,6))

# def example(first,second,third):
#     return first+second+third
# # print(example("hello","hii","heyy"))
# print(example(second="techno",first="royal",third="pvt ltd"))


# arbitary arguments
# *


# def example(a,*b):
#     print(a)
#     print(b)

# example(1,2,3,4,5,6,3,8,9,10,11)





def example(a,*b):
    # print(b,a)
    print(b)
    c=list(b)
    for i in range(len(c)):
        if c[i] == 3:
            c[i] = 33
    return tuple(c)
print(example(1,2,3,4,5,6,7,3,8,9,10,11))
