# OOP

# 1. class and objects
# 2. inheritance
# 3. abstraction
# 4. polymorphism
# 5. encapsulation

# functuon--in buit function
# len(),print(),def examp-le()
# instance

# class Firstsecond:
# class FirstSecond:
#     name='royal'

#     def display(self,a):
#         print(self.name,a)

# obj = FirstSecond()
# obj.display('techno')
# print(obj.name)

# class ExamplePrac:

#     msg="hello from class"

#     def display(self):
#         print(self.msg)
#         return "hello from method display"
    
# ex = ExamplePrac()
# print(ex.msg)
# print(ex.display())

# class Student
# dictionary={'':False}

# class Student:
#     students ={
#         'jainam':False,
#         'krish':False
#     }

#     def take_attendance(self,*name):
#         print(name)
#         # if name in self.students:
#         #     self.students[name] = True
#         # else:
#         #     print("not in dict")
    
#     def show(self):
#         return self.students
    
# obj = Student()
# obj.take_attendance('fgh','dfghjk','dfghj')
# print(obj.show())


class Subject:
    dict1={
    'student1':(),
    'student2':()
    }
    def take_subject(self,name,*subject):
        if name in self.dict1:
            a=list(self.dict1[name])
            a.extend(subject)
            self.dict1[name]=tuple(a)

    def show(self):
        return self.dict1

obj = Subject()
obj.take_subject('student1','python','java')
print(obj.show())

# class Student:
#     student_dict={
#         "deep":False,
#         "vedant": False,
#         "kunj":False
#     }

#     def take_attendance(self,name):
        
#         if name in self.student_dict.keys():
#             self.student_dict[name]=True
    
#     def show_attendance(a):
#         # dict={}
#         # dict.clear
#         # take_attendance()
#         return a.student_dict
    
# student = Student()
# student.take_attendance(input("enter student name"))
# print(student.show_attendance())

