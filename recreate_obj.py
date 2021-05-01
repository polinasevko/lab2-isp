import types
import importlib


def recreate_object(deser_dict, globals, name):
    if name == None:
        return deser_dict
    elif deser_dict[name]["type"] == "function":
        return recreate_function(deser_dict[name], deser_dict, globals)
    elif deser_dict[name]["type"] == "module":
        return recreate_module(deser_dict[name])


def recreate_function(serializable_object, deser_dict, globals):
    serialized_code = serializable_object["code"]

    code = types.CodeType(int(serialized_code["co_argcount"]), int(serialized_code["co_kwonlyargcount"]),
                          int(serialized_code["co_posonlyargcount"]),
                          int(serialized_code["co_nlocals"]), int(serialized_code["co_stacksize"]),
                          int(serialized_code["co_flags"]),
                          bytes(serialized_code["co_code"], "cp1251"), eval(serialized_code["co_consts"]),
                          eval(serialized_code["co_names"]), eval(serialized_code["co_varnames"]),
                          serialized_code["co_filename"], serialized_code["co_name"],
                          int(serialized_code["co_firstlineno"]), bytes(serialized_code["co_lnotab"], "cp1251"))

    additional_obj = {}
    for item in deser_dict:
        if (item in code.co_names and item not in globals):
            additional_obj[item] = recreate_object(deser_dict, globals, item)
    additional_obj.update(globals)

    return types.FunctionType(code, additional_obj)


def recreate_module(py_object):
    return importlib.import_module(py_object["name"])
