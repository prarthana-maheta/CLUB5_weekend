s1 = 'stDudents of this batch are going to rock the INDIAN software industry?'
# print(s1[-11])
# print(s1[30])
# print(s1.count("e",-10,30))
# print(s1.count("are"))
# print(s1.count("europe"))
#
# print(s1.count("z", 20))
# print(s1.count("e", 20, 40))
# print(s1.count("e", -40, -20))

# s1 = 'stDudents of this batch are going to rock the INDIAN software industry?'
# print(s1)
# s2=s1.encode()
# print(s2.capitalize())
# print(s1.encode("utf-16"))
# s2=s1.encode("utf-16")
# print(s2.decode("utf-16"))

s1 = 'stDudents of this batch are going to rock the INDIAN software industry?'
# print(s1.endswith("?"))
# print(s1.endswith("try!"))
# # print(s1.endswith("is", 40))
# # s1.endswith("s", -40, 60)
#
# print(s1.startswith("s"))
# print(s1.startswith("t", 1,3))

s1 = 'students of this batch are going to rock the INDIAN software industry?'

# print(s1.find("D"))
# # # print(s1.find("e"))
# print(s1.index("D"))
# print(s1.rfind("D",))
# print(s1.lfind("D"))
# print(s1.rindex("D"))
# print(s1.lindex("D"))
#



# """
# print(s1.find("D"))
# print(s1.find("e"))
# print(s1.find("rock"))
#
# a = s1.find("e")
# print(s1.find("e", a+1))
#
# print(s1.find("e", 5))
# print(s1.find("e", 5, 30))
#
# print(s1.find("e", 5, -5))
# print(s1.find("Python"))
#
# print()
#
# print(s1.index("D"))
# print(s1.index("e"))
# print(s1.index("rock"))
#
# a = s1.index("e")
# print(s1.index("e", a+1))
#
# print(s1.index("e", 5))
# print(s1.index("e", 5, 30))
#
# print(s1.index("e", 5, -5))
# print(s1.index("Python"))
#
#
# print(s1.rfind("e"))
# print(s1.rfind("are", 20, -3))
# print(s1.rindex("D"))
# print(s1.rindex("r", 20, -20))
# """
#
# # s1 = "Abc"
# # # s2 = "5⁴"
# # # s3 = "②⓪②②"
# # # s4 = "½"
# # # s5 = "二千二十二"
# #
# # # methods starting from is: All these methods return True or False
# #
# # # print(s1.isupper())
# # # print(s1.islower())
# # # print(s1.istitle())
# #
# # s1 = "二千二十"
# # s2 = "AlakhPandya"
# # s3 = "9876543210"
# # # s4 = "AlakhPandya9876543210"
# # # # print(s2.isnumeric())
# # # # print(s2.isalpha())
# # # # print(s4.isalnum())
# # # # print(s3.isdecimal())
# # # # print(s3.isdigit())
# # # # print(s1.isascii())
# # #
# # #
# # # s5 = "₹5000"
# # # s6 = "abdh"
# # # # print(s6.isidentifier())
# # # #
# # # #
# # # s7 = " anbfbvh\t b c"
# # # # print(s7.isspace())
# # # # print(s7.isprintable())
# # #
# # # """
# # # The difference between isnumeric, isdigit & isdecimal
# # # """
# # # """
# # # print(s4.isdecimal())   # only recognizes digits from 0 to 9 and nothing else.
# # # print(s4.isdigit())     # also recognizes subscript, superscript, circled numbers
# # # print(s4.isnumeric())   # also recognizes roman numerals, vulgar fractions, digits from other languages
# # #
# # # print(s5.isnumeric())
# # # """
# # #
# # #
# # #
# # #
# # #
# # # # list(strings)
# # # # [] datatype list
# # # s6 = ('students of this batch aregoing to rock the indian software '
# # #       'industry!\nBecause they are very sincere.\nThey also do their homework on time.        ')
# # # # print(s6)
# # # # print(s6.split(" ")) #return list
# # # # print(s6.split("z"))
# # # # print(s6.split(" ", 4))
# # # #
# # # # print(s6.rsplit(" ",3))
# # # # print(s6.split(" "))
# # #
# # # # # print(s6)
# # # # print(s6.split("\n"))
# # # # print(s6.splitlines())
# # #
# # # # s7 = "Harsh is a good boy.
# # # # But, this sentence has an error."
# # #
# # # s8 = "a"
# # # s9 = s8.join("123")
# # # print(s9)
# # #
# # # # print(" ".join(s8))
# # #
# # # s6 = '            students         of this batch are going batch are to rock the indian software industry!         '
# # # # print(s6.partition("batch"))
# # # # print(s6.partition("are are")) #return tuple
# # # # print(s6.rpartition("batch"))
# # #
# # # # print(s6.strip("s"))
# # # s8 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy$$Birthday!$$$$$$$$$$$$$$$$$"
# # #
# # # print(s8.replace("$", " "))
# #
# # """
# #
# # s8 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy$$Birthday!$$$$$$$$$$$$$$$$$"
# # print(s8.lstrip("$"))
# # print(s8.rstrip("$"))
# # print(s8.strip("$"))
# # """
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # Collections in Python
# # """
# # Ordered     Immutable   string      "ahfahdxsd"
# # Ordered     Mutable     list        [1,2,3]
# # Ordered     Immutable   tuple       (1,2,3)
# # Unordered   Mutable     set         {1,2,3,5}
# # Unordered   Mutable     Dict         {"name":"prarthana"}
# #
# # Two special collections:
# # strings: Ordered & Immutable collections of characters              " "/ ' '
# # dictionaries: Unordered & Mutable collections of key-value pairs
# # """
# #
# # # # list: Ordered & Mutable collection of members
# # # list1=[1,2,3,4,5,6,7,8,91,0]
# # numbers = [33,12, 0, -125, 44, 33, 4791234, -5592, 33]
# # # index     0  1    2     3   4
# # #          -9 -8    -7
# # # print(len(numbers))
# # # print(type(numbers))
# # # s='123456789'
# # # s=123456789
# # # print(list(s))
# # print(numbers[2:8])
# #
# # print altrenate elements from list
# #
# # perform addition between first and last element
# #
# #
# #
# #
# #
# #
# #
# #
# # print(len(numbers)-1)
#
# numbers = [33,12, 0, -125, 44, 33, 4791234, -5592, "33"]
#
# print(min(numbers))
# print(max(numbers))
#
#
