# # decorators

# # function in function 


# # def dec(function_mul):
# #     def inner(a,b):
# #         if a >0 and b>0:
# #             print(function_mul(a,b))
# #     return inner


# # # @dec2
# # @dec
# # def mul(a,b):

# #     return a*b

# # mul(0,1)

# # def __royal__()
# # dunder methods/ special methods

# class Student:
#     def __init__(self):
#         self.name="royal"
#         print("in init")


#     def __call__(self):
#         print("in call")

#     def __str__(self):
#         return "you are not smart then me"
    
#     # def display(self):
#     #     return self.name

# student = Student()
# # student()
# print(student)

# # print(student.name)
# # print(student.display())
# # student.__init__()


# Write a Python class BankAccount with attributes 
# like  {a dictionary account_number: balance }
# and methods like deposit, withdraw, and check_balance.

# key point: dict in Init 
#             use self 
#             IF conditions when required

# Write a Python class Employee with 
# attributes like emp_id, emp_name, emp_salary, and emp_department and 
# methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: hours_worked, emp_id
# which is the number of hours worked by the employee. If the number of hours worked
# is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))