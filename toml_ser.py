import toml
from get_obj import get_dict_to_ser
from recreate_obj import create_object


class Toml:

    def dump(self, obj, fp):
        ser_dict = get_dict_to_ser(obj)
        with open(fp, 'w') as toml_file:
            toml.dump(ser_dict, toml_file)

    def dumps(self, obj):
        ser_dict = get_dict_to_ser(obj)
        toml_str = toml.dumps(ser_dict)
        return toml_str

    def load(self, fp, name = None):
        with open(fp, 'r') as toml_file:
            deser_dict = toml.load(toml_file)
        obj = create_object(deser_dict, globals(), name)
        return obj

    def loads(self, toml_str, name = None):
        deser_dict = toml.loads(toml_str)
        obj = create_object(deser_dict, globals(), name)
        return obj
