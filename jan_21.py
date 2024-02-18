# looping:
# remove duplicates
# abc='1234556'
# list1=list(abc)
# list2=[]
for i in range(1,100):
    if i not in list2:
        print(i)
        list2.append(i)
#
# print(''.join(list2))
# print(list2)
# print(str(list2))

# keywords for looping:
# break
# continue
# pass
# a=10
# list1=[1,2,3,10,3,4,10]
# #
# for i in list1:
#
#     if i==10:
#         pass
#         print(i)
a=10
list1=[1,2,10,10,3,4,10]
for i in range(len(list1)):
    print(list1[i])
    if list1[i] ==10:
        print(i)

# Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4


# Write a Python program that prints all the numbers except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

#  Write a Python program to print the alphabet pattern 'E'.
# Expected Output:
#
#  *****
#  *
#  *
#  ****
#  *
#  *
#  *****
# list1=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(list1)):
#     for j in list1[i+1:]:
#         print(j)

# Write a Python program to sum two integers.
# However, if the sum is between 15 and 20 it will return 20.

# print(range(15,20)))

# Write a Python program that checks whether a string represents an integer or not.
# Expected Output:
# # i.isdigit()
# Input a string: Python1
# The string is  an integer.

inp_str =input()
for i in inp_str:
    if i.isdigit():
        print("integer")
        break
    else:
        continue