import functools
def log_with_arg(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            print("%s %s"%(text,fn.__name__))
            return fn(*args,**kwargs)
        return wrapper
    return decorator

def log_no_arg(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        print("%s"%fn.__name__)
        return fn(*args,**kwargs)
    return wrapper

def log(arg):
    if hasattr(arg,'__call__'):
        fn = log_no_arg(arg)
    else:
        fn = log_with_arg(arg)
    return fn

#test
@log('this is function')
def add(a,b):
    return a + b

@log('this is function')
def minus(a,b):
    return a - b

add(1,2)
minus(2,1)

