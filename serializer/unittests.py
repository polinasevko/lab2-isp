import unittest
import test
from fabric import SerializerFactory

fact = SerializerFactory()


class TestSerializer(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)

    def test_base_object(self):
        obj_list = [test.objects, test.string, test.o1, test.o2]
        for obj in obj_list:
            for ser in fact.get_ser_list():
                dumped_str = ser.dumps(obj)
                new_obj = ser.loads(dumped_str)
                self.assertEqual(obj, new_obj)

    def test_functions(self):
        obj_list = [test.simple_func, test.func_with_globals, test.func_with_builtins, test.log_module]
        obj_list_arg = [test.list_returner, test.dict_returner,
                        test.func_with_args_sum, test.simplelambda,
                        test.exponent_module]
        for obj in obj_list:
            for ser in fact.get_ser_list():
                dumped_str = ser.dumps(obj)
                new_obj = ser.loads(dumped_str)
                self.assertEqual(obj(), new_obj())
        for obj in obj_list_arg:
            for ser in fact.get_ser_list():
                dumped_str = ser.dumps(obj)
                new_obj = ser.loads(dumped_str)
                self.assertEqual(obj(5), new_obj(5))

    def test_json_file(self):
        obj = test.simple_func
        ser_json = fact.get_serializer("json")
        ser_json.dump(obj, "file.json")
        new_obj = ser_json.load("file.json")
        self.assertEqual(obj(), new_obj())

    def test_pickle_file(self):
        obj = test.simple_func
        ser_pickle = fact.get_serializer("pickle")
        ser_pickle.dump(obj, "file.pickle")
        new_obj = ser_pickle.load("file.pickle")
        self.assertEqual(obj(), new_obj())

    def test_yaml_file(self):
        obj = test.simple_func
        ser_pickle = fact.get_serializer("yaml")
        ser_pickle.dump(obj, "file.yaml")
        new_obj = ser_pickle.load("file.yaml")
        self.assertEqual(obj(), new_obj())


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromModule(json_tests)
    # sys.stdout = open(os.devnull, 'w')
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # sys.stdout = sys.__stdout__
