from get_obj import get_dict_to_ser
import json
import numpy

def f(a, b):
    return a + b



def func():
    print(numpy.arccos(0))

dict_to_ser = get_dict_to_ser(f)
str  = json.dumps(dict_to_ser)
print(str)


