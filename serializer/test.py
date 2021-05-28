import logging
import math

o1 = [[[[[[[[[[[3, [[[[[[[[[[[[[[[[[[[[[[[[[[[55.3, [[[[[[[[[[4]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

o2 = {'2': ['5', '3']}

objects = [{}, []]

string = "hi beach"


def simple_func():
    pass


gl1 = 100


def func_with_globals():
    return gl1


def func_with_builtins():
    print(simple_func)


def list_returner(a):
    x = a * 2
    y = a + 10
    return [x, y]


def dict_returner(a):
    x = a * 2
    y = a + 10
    return {x: y}


def func_with_args_sum(*args):
    return sum(args)


simplelambda = lambda x: x + x


def log_module():
    logging.info("hello im serializer")


def exponent_module(x):
    return math.exp(x)
