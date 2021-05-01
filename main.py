
import json_ser

al = [2, 19]

def f(a, b):
    return a + b

def func():
    pass

ser = json_ser.Json()

ser.dump(f, "func.json")

json_obj = ser.load("func.json", "f")
print(json_obj(6, 19))

ser.dump(al, "func.json")

json_obj = ser.load("func.json", )





