#implementation of decorator function
def decorator_function(orginal_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(orginal_function.__name__))
        return orginal_function(*args, **kwargs)
    return wrapper_function

#implementation of  the decorator class
class decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_function
def display():
    print("Display function ran")

@decorator_function
def display_info(name, age):
    print("Display_info ran with arguments ({}, {})".format(name, age))

#display_info("John", 25)

@decorator_class
def display__():
    print("Display function ran")

@decorator_class
def display_info__(name, age):
    print("Display_info ran with arguments ({}, {})".format(name, age))

display__()