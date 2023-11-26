# # Datatypes in Python:
# """
# Numeric: int, float, complex
# a = 7 + 3i, b = 5 + 7i
# (7 + 3i)(5 + 7i)
#
#
# a = 7 + 3j
# b = 5 + 7j
# print(a * b)
#
#
# collections:
# string: Ordered & Immutable Collection Of Characters
# """
s1='Students of this batch are going to rock the INDIAN software industry!'
a='123'
b=124
# print(type(b))
# # index: 	 0123456789..................
# # -ve index
# # :	 ......................................................987654321
print(s1[-2])
# # print(type(s1))
# print(s1)
# s1[0]='1'
# print(s1)
# print(s1[len(s1)-1])
# s1='0123456789'
# 1: odd numbers
# 2: eveen numbers
# 3: addtion of first and last index
# 4: print 4 to 9


s1='Students of this batch are going to rock the INDIAN software industry!'
# s2=s1[:11:-2]
# s2=s1[1:-11:-2]
# s3=s1[-10:21:-1]
# print(s2)
# print(s3)
# s2=s1[:7:2]
# print(s1[:7:2])
# print(s1)
# print(s2)
# s1="1=====100 fesfsrsdfcfghdre"
#
# # print(s1[:100])
# # s1[0]='1'
# # print(s1)
# # # # slicing
# # s2 = s1[9 : 69]
# # print(s1)	# Slicing will always return new data
# # print(s2)
#
# # print(s1[600])
# # print(s1[12 : 600])
# # print(s1[12 : ])
# # print(s1[ : 60])
# # print(s1[ : ])
#
# # print(s1[60])
# # print(s1[-3])
# """
# print(s1[0])
#
# print(s1[30 : 3])
# print("The end")
# print(s1[-25 : -5])
# print(s1[-30 : 50])
# print(s1[30 : -3])
#
# print(s1[4 : -3])
#
#
# print(s1[3 : 55 : 3])
# print(s1[55 : 3 : -1])
# print(s1[ : : -1])
# print(s1[ : : -3])
# print(String[1:5:2])
# """
#
# # methods vs. functions
# # function_name(oprand)
# # oprand.method_name(arguments)
#
# # Case related methods:
# #slice
# s1='ROYAL TECHNOSOFT limited'

# # ROYAL
# # TECHNOSOFT
# # limited
# # ROYAL limited
#
#
#
#
#
#
#
# # s2=s1[:5]
# # s3=s1[-7:]
# # print(f"{s2} {s3}")
# # Output:
#
#
#
#
# # *****New task to perform********
#
# s1='strings are IMMUTABLE so, methods of strings cannot change the original string. Instead'
# #
# # Output:- 1) print IMMUTABLE using slicing s1[12:22
# #          2) print Insted using slicing
# #          3) skip alternate character and print the new string
#
# # print(s1[12:22])
# # print(s1[-7:])
# # print(s1[::2])
#
#
# # 'Royal Technosoft Limited'
# # 'I am learning python'
#
# # print(s2)
#
# # indian
# # royal
# # technosoft
# 'Students of this batch are going to rock the INDIAN software industry!'
# s1='students .of this batch are going to rock the INDIAN software industry!'
#
#
# output: s1 bdha first letters capitilize
#         indian in lower case
#         all the s1 string should in upper case
#         all the s1 string should be in lower case
#         software industry  in uppercase
#
# # indian
#
# # s1[5]='abc'
# print(s1)
s1='students .of this batch are going to rock the INDIAN software industry!'
#
# 1: convert s1 in uppercase
# 2: convert INDIAN in lower case
# 3: reverse the s1 in upeercase
# 4: make s1 in title and lower
#
print(s1)
print(s1.capitalize())
# # # print(len(s1))
# # # # print(s2)	# strings are immutable so, methods of strings cannot change the original string. Instead, they will return a new string.
# # # print( s1.capitalize())
# # # # # print( s1[5].capitalize())
# # print(s1.upper())
# print(s1.lower().title().upper())
# print(s1.swapcase())
# print(s1.title())
#
# len(s1)
# print()
# input()
# type()

s1 = 'DtDudents of this batch are going to rock the INDIAN software industry?'
# s2 = "What is ß"

# print(s2.lower())
# print(s1)
# print(s1.casefold())

s3 = s1.center(80,"@")
print(s3)
print(s1.rjust(100, "*"))
print(s1.ljust(100, "-"))
# print(s3)
# Alignment related methods