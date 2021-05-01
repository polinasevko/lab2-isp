import json
from get_obj import get_dict_to_ser
from recreate_obj import recreate_object


class Json:

    def dump(self, obj, fp):
        ser_dict = get_dict_to_ser(obj)
        with open(fp, 'w') as json_file:
            json.dump(ser_dict, json_file)

    def dumps(self, obj):
        ser_dict = get_dict_to_ser(obj)
        return json.dumps(ser_dict)

    def load(self, fp, name):
        with open(fp, 'r') as json_file:
            return recreate_object(json.load(json_file), globals(), name)

    def loads(self, json_str, name):
        return recreate_object(json.loads(json_str), globals(), name)
