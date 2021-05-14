from json_ser import Json
from pickle_ser import Pickle
from yaml_ser import Yaml
from toml_ser import Toml


class SerializerFactory:
    def __init__(self):
        self.serializersList = {
            "json": Json(),
            "pickle": Pickle(),
            "toml": Toml(),
            "yaml": Yaml()
        }

    def set_serializer(self, name, value):
        self.serializersList.setdefault(name, value)

    def get_serializer(self, name):
        serializer = self.serializersList.get(name)
        if serializer is None:
            raise ValueError()
        else:
            return serializer
