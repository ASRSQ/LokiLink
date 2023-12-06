import random

def singleton(class_):
    instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return wrapper

def get_indexes_list_except(length, index):
    return [i for i in range(length) if i != index]

def get_random_index_except(length, index):
    indexes = get_indexes_list_except(length, index)
    random_index = random.choice(indexes)
    return random_index

def get_indexes_list(length):
    return [i for i in range(length)]

def get_random_index(length):
    indexes = get_indexes_list(length)
    return random.choice(indexes)
