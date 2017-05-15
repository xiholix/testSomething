from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
import time
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


if __name__ == "__main__":
    test()