import types


def get_dict_to_ser(obj, name="None"):
    if isinstance(obj, types.FunctionType):
        return serialize_function(obj)
    elif isinstance(obj, types.ModuleType):
        return serialize_module(obj)
    elif isinstance(obj, (int, float, bool, str, list, dict, type(None))):
        return {name: {"type": "base", "obj": obj}}
    else:
        raise ValueError("Can't serialise such object.")


def serialize_function(obj):
    dictionary = {obj.__name__: {
        "type": "function",
        "name": f"{obj.__name__}",
        "qualname": f"{obj.__qualname__}",
        "annotations": f"{obj.__annotations__}",
        "kwdefaults": f"{obj.__kwdefaults__}",
        "defaults": f"{obj.__defaults__}",
        "module": f"{obj.__module__}",
        "doc": f"{obj.__doc__}",
        "closure": f"{obj.__closure__}",
        "globals": f"{obj.__globals__}",
        "code": {
            "co_argcount": f"{obj.__code__.co_argcount}",
            "co_kwonlyargcount": f"{obj.__code__.co_kwonlyargcount}",
            "co_posonlyargcount": f"{obj.__code__.co_posonlyargcount}",
            "co_nlocals": f"{obj.__code__.co_nlocals}",
            "co_stacksize": f"{obj.__code__.co_stacksize}",
            "co_flags": f"{obj.__code__.co_flags}",
            "co_code": obj.__code__.co_code.decode("cp1251"),
            "co_consts": f"{obj.__code__.co_consts}",
            "co_names": f"{obj.__code__.co_names}",
            "co_varnames": f"{obj.__code__.co_varnames}",
            "co_filename": f"<stdin>",
            "co_name": f"{obj.__code__.co_name}",
            "co_firstlineno": f"{obj.__code__.co_firstlineno}",
            "co_lnotab": obj.__code__.co_lnotab.decode("cp1251"),
            "co_freevars": f"{obj.__code__.co_freevars}",
            "co_cellvars": f"{obj.__code__.co_cellvars}"
        }
    }
    }
    dictionary = update_globals(obj, dictionary)
    return dictionary


def update_globals(obj, dictionary):
    for additional_obj in obj.__globals__:
        if additional_obj in obj.__code__.co_names:
            dictionary.update(get_dict_to_ser(obj.__globals__[additional_obj], additional_obj))
    return dictionary


def serialize_module(obj):
    dictionary = {obj.__name__: {"type": "module", "name": obj.__name__}}
    return dictionary
