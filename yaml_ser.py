import yaml
from get_obj import get_dict_to_ser
from recreate_obj import create_object


class Yaml:

    def dump(self, obj, fp):
        ser_dict = get_dict_to_ser(obj)
        with open(fp, 'w') as yaml_file:
            yaml.dump(ser_dict, yaml_file)

    def dumps(self, obj):
        ser_dict = get_dict_to_ser(obj)
        yaml_str = yaml.dumps(ser_dict)
        return yaml_str

    def load(self, fp, name = None):
        with open(fp, 'r') as yaml_file:
            deser_dict = yaml.safe_load(yaml_file)
        obj = create_object(deser_dict, globals(), name)
        return obj

    def loads(self, yaml_str, name = None):
        deser_dict = yaml.loads(yaml_str)
        obj = create_object(deser_dict, globals(), name)
        return obj
