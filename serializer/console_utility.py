from os import path

from argparser import get_file
from fabric import SerializerFactory


def main():
    format, files = get_file()
    factory = SerializerFactory()
    out_ser = factory.get_serializer(format)
    for file in files:
        file_name, extension = path.splitext(file)
        if format != extension[1:]:
            in_ser = factory.get_serializer(extension[1:])
            obj_dict = in_ser.load(file)
            out_ser.dump(obj_dict, f'{file_name}.{format}')


if __name__ == "__main__":
    main()
