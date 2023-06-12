import functools

def save_info(original_func):
    """Decorator that saves information about the decorated function"""
    def decorated_func(*args, **kwargs):
        # Do something before the original function is called
        result = original_func(*args, **kwargs)
        # Do something after the original function is called
        return result

    # Set attributes on the decorated function
    decorated_func.__name__ = original_func.__name__
    decorated_func.__doc__ = original_func.__doc__
    decorated_func.__original_func = original_func

    return decorated_func

def print_result(func):
    @save_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)