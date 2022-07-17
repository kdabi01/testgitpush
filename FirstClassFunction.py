
def square(x):
    return x*x
f = square

def cube(x):
    return x * x * x

#print(f(5))
#print(square)

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

my_list = ["aaaa", "bb", "c", "dddd"]

#print(my_map(len, my_list))

def logger(msg):
    def log_message():
        print("Log: ", msg)
    return log_message

log_hi = logger("Hi")
log_hi()