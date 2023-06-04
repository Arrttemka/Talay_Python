import math
from Talay_serializer.serializer_zavod import zavod
from Talay_serializer import serializer_zavod

def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def class_meth(cls):
        return math.pi
    @property
    def prop(self):
        return self.a * self.b




class C(A, B):
    pass

#ser = serializer_zavod.zavod.create_zavod('json')

#ser.dump(, open('test_2.json', 'w'))

ser = zavod.create_zavod('json')




var = 15
var_ser = ser.dumps(var)
var_des = ser.loads(var_ser)
print(var_des)



C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)



c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())



f = C(1, 2)
print(f.my_sin(11))
