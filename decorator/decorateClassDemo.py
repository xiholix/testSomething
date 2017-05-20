# --*--coding:utf8--*--
import functools


def decorate(*args):
    print(args)

    def dec(function):
        print('in dec')
        @property  #如果有这个，则调用时不能用函数调用方式，否则会出现错误
        # TypeError: 'NoneType' object is not callable
        @functools.wraps(function)
        def de(self):
            print('hello')
            function(self)
        return de
    return dec


def double_wrapper(function):
    print('in double_wrapper')

    @functools.wraps(function)
    def decorator(*args, **kwargs):
        print(args)
        return function(args[0])

    return decorator


def doublewrap(function):
    """
    A decorator decorator, allowing to use the decorator to be used without
    parentheses if not arguments are provided. All arguments must be optional.
    """
    print("in doublewrap")
    @functools.wraps(function)
    def decorator(*args, **kwargs):
        print(args)
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return function(args[0])
        else:
            # return lambda wrapee: function(wrapee, *args, **kwargs)
            print(args)
            return lambda t: function(t, *args, **kwargs)
    return decorator


def testWrap(function):
    # @functools.wraps(function)
    def decorator(*args, **kwargs):
        print('in decorator '+str(args))
        print(function.__name__)
        def t(test):
            print(' in t')
            print(args)
            print(test.__name__)
            return function(test, *args, **kwargs)
        return t
    return decorator


@testWrap
def new_decorate(function, *args):  #直接使用这个修饰符号如果通过括号传参会报错,
    #AttributeError: 'int' object has no attribute '__module__'
    print('in new_decorate '+str(args))
    @property
    # @functools.wraps(function)
    def de(self):
        print('hello')
        print(function.__name__)
        function(self)

    return de





class Demo(object):

    def __init__(self):
        pass

    @decorate()
    def test(self):
        print("in test")
    @new_decorate(1,2)
    def test2(self):
        print('in test2')

def fnTest(var, *args):
    print var
    print(args)

def outFn(*args):
    print(args)
    def innerFn(*args):
        return fnTest()


if __name__ == "__main__":
    d = Demo()
    a = d.test2
    print(a)
    # d.test
    print('d')
    # t = outFn(1,2,4)
