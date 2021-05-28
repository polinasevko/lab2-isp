import json
from get_obj import get_dict_to_ser
from recreate_obj import create_object


class Json:

    def dump(self, obj, fp):
        ser_dict = get_dict_to_ser(obj)
        with open(fp, 'w') as json_file:
            json.dump(ser_dict, json_file)

    def dumps(self, obj):
        ser_dict = get_dict_to_ser(obj)
        json_str = json.dumps(ser_dict)
        return json_str

    def load(self, fp):
        with open(fp, 'r') as json_file:
            deser_dict = json.load(json_file)
        obj = create_object(deser_dict, globals(), list(deser_dict.keys())[0])
        return obj

    def loads(self, json_str):
        deser_dict = json.loads(json_str)
        obj = create_object(deser_dict, globals(), list(deser_dict.keys())[0])
        return obj
