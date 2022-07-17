#Decorators
def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func
@decorator_func
def display_func():
    print("display function run")
@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info("kamlesh", 30)

#decorator_display = decorator_func(display_func)
#decorator_display()

#display_func()