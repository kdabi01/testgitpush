from functools import wraps


def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)
    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
        logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)
    return wrapper_func

def my_timer(original_func):
    import time
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(original_func.__name__, t2))
        return  result
    return wrapper

import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(5)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info("Tim", 33)