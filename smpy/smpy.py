import inspect
from forbiddenfruit import curse
import smpy.collections.smpy_list

def sm_list():
    for each in [func for func in inspect.getmembers(smpy_list, predicate=inspect.isfunction)]:
        curse(list, each[0], each[1])
