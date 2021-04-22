from get_obj import get_dict_to_ser
from recreate_obj import recreate_object
import json
import numpy

def f(a, b):
    return a + b



def func():
    numpy.arccos(0)

dict_to_ser = get_dict_to_ser(f)
str  = json.dumps(dict_to_ser)
json_obj = recreate_object(json.loads(str), globals(), "f")




