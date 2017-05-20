# -*-coding:utf8-*-
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
#
#
'''
@version: ??
@author: xiholix
@contact: x123872842@163.com
@software: PyCharm
@file: explainDecorator.py
@time: 17-5-20 下午3:05
'''
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import


def wrapper(function):
    def fun(*args, **kwargs):
        print('in wrapper, you add to do something')
        return function(*args, **kwargs)

    return fun


@wrapper
def decoratored(*args, **kwargs):
    print('in fun, args is {0}, kwargs is {1}'.format(str(args), str(kwargs)))

def test_wrapper():
    decoratored(1,2, a=2)

def double_wrapper(function):
    def decorator(*args, **kwargs):
        if len(args)==1 and len(kwargs)==0 and callable(args[0]):
            return function(args[0])
        else:
            def fn( decoratedFn):
                # print('in double_wrapper fn decorator, args is {0}, kwargs is {1}'.format(str(args1), str(kwargs1)))
                return function(decoratedFn, *args, **kwargs)
            return fn
    return decorator

@double_wrapper
def first_double_wrapper(function, *args, **kwargs):

    def decorator(*args1, **kwargs2):
        print('in first_double_wrapper decorator, args is {0}, kwargs is {1}'.format(str(args), str(kwargs)))
        print('in first_double_wrapper decorator, args is {0}, kwargs is {1}'.format(str(args1), str(kwargs2)))
        return function(*args1, **kwargs2)
    return decorator




def first_wrapper(*args, **kwargs):

    def decorator(function):
        print('this is execute only once')
        def func(*args1, **kwargs1):
            print('wrapper argments is ' + str(args) + " kwargs is " + str(kwargs))
            print('in wrapper, you add to do something')
            return function(*args1, **kwargs1)

        return func

    return decorator





def test_first_wrapper():
    @first_wrapper(1, 2, c=12)
    def decoratored2(*args, **kwargs):
        print('in fun, args is {0}, kwargs is {1}'.format(str(args), str(kwargs)))

    decoratored2(2,3,4, b=5)
    decoratored2(2, 3, 4, b=5)


def test_second_wrapper():
    @first_double_wrapper(2,3)
    def decoratored2(*args, **kwargs):
        print('in fun, args is {0}, kwargs is {1}'.format(str(args), str(kwargs)))
    decoratored2(2,3,5, b=7)

if __name__ == "__main__":
    # test_wrapper()
    # test_first_wrapper()
    test_second_wrapper()