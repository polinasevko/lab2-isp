import math
import logging

t1 = [[[[[[[[[[[3, [[[[[[[[[[[[[[[[[[[[[[[[[[[55.3, [[[[[[[[[[4]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

t2 = {'2': ['5', '3']}

objects = [{}, []]

string = "hi beach"


def simple_func():
    pass

gl1 = 53


def func_with_globals_and_builtins():
    print(simple_func)
    return gl1

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


def func_with_args_d(**args):
    return args


simplelambda = lambda x: x * x


def a_module(x):
    return math.sin(x)


def b_module():
    logging.info("hello")
