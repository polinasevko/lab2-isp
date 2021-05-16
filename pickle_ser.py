import pickle
from get_obj import get_dict_to_ser
from recreate_obj import create_object


class Pickle():

    def dump(self, obj, fp):
        ser_dict = get_dict_to_ser(obj)
        with open(fp, 'wb') as pickle_file:
            pickle.dump(ser_dict, pickle_file)

    def dumps(self, obj):
        ser_dict = get_dict_to_ser(obj)
        pickle_str = pickle.dumps(ser_dict)
        return pickle_str

    def load(self, fp):
        with open(fp, 'rb') as pickle_file:
            deser_dict = pickle.load(pickle_file)
        obj = create_object(deser_dict, globals(), list(deser_dict.keys())[0])
        return obj

    def loads(self, pickle_str):
        deser_dict = pickle.load(pickle_str)
        obj = create_object(deser_dict, globals(), list(deser_dict.keys())[0])
        return obj
