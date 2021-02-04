import numpy as np
import math as mt

print('Question 2: Floating Point Accuracy')
print('\n')
print('Part A:')

print('\n')

print('Part B:')
print('A + B - A should equal B')
a = 1.2 ; a = np.int(a)
b = 1.0 ; b = np.int(b)
print('For a = 1.2 and b = 1.0 this should be one regardless of int rounding')
intanswer = a + b - a
print('The integer: 1.2 + 1.0 - 1.2 = ',intanswer)
print('\n')
print('For floating point values a = 1.2 and b = 1.0:')
x = 1.2 ; x = np.float(x)
y = 1.0 ; y = np.float(y)
floatanswer = x + y - x
print('1.2 + 1.0 - 1.2 = ',floatanswer)
print('\n')

print('Part C:') #Does not work correctly
print('Bad float compare using a = 1 and b = 1 + 1e-14*sqrt(2)')
def bad_float_compare(a,b, dtype = float):
    assert(a == b),"These values as floats are not equal."
    if a == b:
       return True
m = 1.0
n = 1 + 1e-14*mt.sqrt(2)
badanswer = bad_float_compare(m,n)

def good_float_compare(a,b, dtype = float):
    assert(a != b),"The values as floats are equal"
    if a != b:
        return True
q = 1.0
w = 2.0 + 1.0 - 2.0
goodanswer = good_float_compare(q,w)
print(goodanswer)



