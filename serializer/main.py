from fabric import SerializerFactory
import math
import logging

def using_logging_module():
    logging.info("hello")

def f(x):
    return math.sin(x)

qwerty = 12
def emp_f(a=3):
    return qwerty + a

a = [5, qwerty]

fact = SerializerFactory()

serializer_json_emp_fu = fact.get_serializer("json")
# serializer_json_fu = fact.get_serializer("json")
serializer_json_base_obj = fact.get_serializer("json")
serializer_json_emp_fu.dump(emp_f, "emp_fu.json")
json_emp_fu = serializer_json_emp_fu.load("emp_fu.json")
# serializer_json_fu.dump(f, "fu.json")
# json_fu = serializer_json_fu.load("fu.json")
serializer_json_base_obj.dump(a, "base_obj.json")
json_base_obj = serializer_json_base_obj.load("base_obj.json")

#print(json_emp_fu())
# print(json_fu(math.pi / 4))
#print(json_base_obj)


serializer_pickle_emp_fu = fact.get_serializer("pickle")
# serializer_pickle_fu = fact.get_serializer("pickle")
serializer_pickle_base_obj = fact.get_serializer("pickle")
serializer_pickle_emp_fu.dump(emp_f, "emp_fu.pickle")
pickle_emp_fu = serializer_pickle_emp_fu.load("emp_fu.pickle")
# serializer_pickle_fu.dump(f, "fu.pickle")
# pickle_fu = serializer_pickle_fu.load("fu.pickle")
serializer_pickle_base_obj.dump(a, "base_obj.pickle")
pickle_base_obj = serializer_pickle_base_obj.load("base_obj.pickle")
#
#print(pickle_emp_fu())
# print(pickle_fu(math.pi / 4))
print(pickle_base_obj)
#
#
serializer_yaml_emp_fu = fact.get_serializer("yaml")
# serializer_yaml_fu = fact.get_serializer("yaml")
serializer_yaml_base_obj = fact.get_serializer("yaml")
serializer_yaml_emp_fu.dump(using_logging_module, "emp_fu.yaml")
yaml_emp_fu = serializer_yaml_emp_fu.load("emp_fu.yaml")
# serializer_yaml_fu.dump(f, "fu.yaml")
# yaml_fu = serializer_yaml_fu.load("fu.yaml")
serializer_yaml_base_obj.dump(a, "base_obj.yaml")
yaml_base_obj = serializer_yaml_base_obj.load("base_obj.yaml")
#
#print(yaml_emp_fu())
# print(yaml_fu(math.pi / 4))
#print(yaml_base_obj[0] * yaml_base_obj[1])
#
#
serializer_toml_emp_fu = fact.get_serializer("toml")
# serializer_toml_fu = fact.get_serializer("toml")
serializer_toml_base_obj = fact.get_serializer("toml")
serializer_toml_emp_fu.dump(emp_f, "emp_fu.toml")
toml_emp_fu = serializer_toml_emp_fu.load("emp_fu.toml")
# serializer_toml_fu.dump(f, "fu.toml")
# toml_fu = serializer_toml_fu.load("fu.toml")
serializer_toml_base_obj.dump(a, "base_obj.toml")
toml_base_obj = serializer_toml_base_obj.load("base_obj.toml")

#print(toml_base_obj)
#print(toml_base_obj)
#print(toml_emp_fu())
