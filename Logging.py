# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

import logging
import LoggingEmployee

#logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#log format
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

#file handler configuration
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")
    else:
        result

num1 = 20
num2 = 0

add_result = add(num1, num2)
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

subtract_result = subtract(num1, num2)
logger.debug('Subtract: {} - {} = {}'.format(num1, num2, subtract_result))

multiply_result = multiply(num1, num2)
logger.debug('Multiply: {} * {} = {}'.format(num1, num2, multiply_result))

divide_result = divide(num1, num2)
logger.debug('Add: {} / {} = {}'.format(num1, num2, divide_result))