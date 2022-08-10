DAY - 5

..............INHERITANCE...........

Inheritance two types = SINGLE INHERITANCE AND MULTI LEVEL INHERITANCE

SINGLE INHERITANCE: It consists of only two classes
Example -    class A:                //It is a parent class or super class
                def f1(self)
                  print('A')
             class B(A):         ///It is a child class
                def f2(self)
                  print('B')
             ob=B()     
             ob.f1()
             ob.f2()

MULTI LEVEL INHERITANCE: in it more than two classes can be used
Example - class A()
            def f1(self)
              print('A')
          class B(A)
            def f2(self)
              print('B')
          class C(B)
            def f3(self)
              print('C')
          ob=c
          ob=f1
          ob=f2
          ob=f3

MULTIPLE INHERITANCE: In it two classes can be accesed by a single class like C(A,B)

Exapple -  class A()
            def f1(self)
              print('A')
          class B()
            def f2(self)
              print('B')
          class C(A,B)
            def f3(self)
              print('C')
          ob=c
          ob=f1
          ob=f2
          ob=f3


HIERARICHAL:In it two classes depend on one class like in given example B and C has properties of A and
             if we create object of c then f2 will not execute because C has not properties of B class
Example - class A()
            def f1(self)
              print('A')
          class B(A)
            def f2(self)
              print('B')
          class C(A)
            def f3(self)
              print('C')
          ob=c
          ob=f1
          ob=f3


HYBRID: It includes both MULTI LEVEL and HIERARICHAL inheritance

NOTE  - Super keyword is used to access variables of parent class in child class

Example - class A():
           a=10
           b=20
           def_init_(self,a,b):
             print('a')
           def f1(self):
             print('m1')
          class B(A)
           a=4
           b=5
           def init(self):
             super().init(12,12)
			print('h')


          def m2(self):
             super().m1()
             print(self.a,self.b)
             print(super().a,super().b)
         ob=b()
         ob.m1()
         ob.m2()



                       .............POLYMORPHISM.............



Two types - Compile time (Overloading) and Run time (Overwriting)
Note:Python doesnt support the concept of overloading 

Example - class A:
           a=10
           b=20
           def_init_(self):
             print('a')
           def f1(self):
             print('m1')
          class B(A)
           a=4
           b=5
           def f1(self):
             print('B class')
          ob=b()
          ob.f1()



                      .............MODULE USE IN PYTHON............


Example - from math import *      // sqrt()
          import math as m        // m.sqrt()
          import math 