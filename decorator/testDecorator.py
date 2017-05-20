from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
import time
import functools
'function decorator'
def test_time(inputFunc):

    def timed(*args, **kwargs):
        startTime = time.time()

        result = inputFunc(*args, **kwargs)

        print("method name{0}, args {1}, kwargs {2}, "
              "elapse time {3}".format(inputFunc.__name__,
                                       args,
                                       kwargs,
                                       time.time()-startTime) )

        return result

    return timed


@test_time
def to_decorate(*args, **kwargs):
    for i in xrange(10000):
        pass

def test():
    to_decorate(1,2,3, 5, {'a':12}, c=15)
    '''
    method nameto_decorate, args (1, 2, 3, 5, {'a': 12}), kwargs {'c': 15}, elapse time 0.000112771987915
    '''

def decorator(function):
    attribut = '_cache'+function.__name__
    print(attribut)
    @property
    @functools.wraps(function)
    def dd(self):
        print('dd')
        if not hasattr(self, attribut):
            print('2')
            setattr(self, attribut, function(self))
        return getattr(self, attribut)
        # function(self)
    return dd


class TestProperty(object):
    def __init__(self):

        self.hello

    @decorator
    def hello(self):
        print(1)
        print('in hello')
        return 'hello world'

    @decorator
    def he(self):
        pass


def test_property():
    a = TestProperty()

    print(a.hello)
    print(a.hello)

if __name__ == "__main__":
    # test()
    test_property()