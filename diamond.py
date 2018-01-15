# Diamond-shaped problem with inheritance
#    A
#  /   \
# B     C
#  \   /
#    D
# Case 1 - method will not be overridden in class B and class C
# Case 2 - method will be overridden in class B but not class C
# Case 3 - method will be overridden in class C but not class B
# Case 4 - method will be overridden in both class B and class C

class A:
    def method(self):
        print('Method: class A')

class B(A):
    def method(self):
        print('Method: class B')

class C(A):
    def method(self):
        print('Method: class C')

class D(B, C):
    pass

d = D()
d.method()