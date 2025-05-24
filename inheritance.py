#Inheritance is a way of creating a new class from an existing calss
#Syntax
#-------
'''
class A:
   #code
class B(A):
   #code
'''


class A:
    print("*")
class B(A):
    print("*")
class C(B):
    print("*")

o = C()
o = B()
o = A()

