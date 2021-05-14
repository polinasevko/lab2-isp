from fabric import SerializerFactory

def f(a, b):
    return a + b

def func():
    pass

a = {'1': 1,
     '2': 'string'}


fact = SerializerFactory()

serializer_json = fact.get_serializer("json")
serializer_json.dump(f, "file.json")


json_obj_1 = serializer_json.load("file.json", 'f')


serializer_json.dump(a, "file.json")
json_obj_2 = serializer_json.load("file.json", None)


print(json_obj_1(4, 5))

print(json_obj_2)

