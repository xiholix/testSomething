# --*--coding:utf8--*--
'Method decorators allow overriding class properties by decorating,'
'without having to find the calling function.'

import functools

def wraper(arg1, arg2):

    def innerFunction(inputFunc):
        print(arg1)
        print(arg2)
        print("inner function")

        @functools.wraps(inputFunc)
        def wra(t, *args, **kwargs):
            print(t)
            result = inputFunc(*args, **kwargs)
            print( 'wra')
            def non():
                print('in non')
                return 'yes'

            return non

        return wra
    return innerFunction


@wraper(1,2)
def test(*args, **kwargs):
    print('test'+str(args))
    return 'test'

'''
根据对这里的代码的理解，使用functools的wraps时只有该修饰符号后定义的函数才需要与被修饰的函数的函数签名
一样。而且只有该被修饰的函数才会多次执行，其他外面的函数内容只会执行一次。因为只有最里面的函数return的东西才会
被多次return，外面的函数都是return他的结果。猜测是因为被修饰的函数最后会变成最里面返回的那个函数，所以相当于
每次执行最里面的那个函数
而且感觉method修饰和函数修饰没什么区别，因为method修饰是对类的方法进行修饰，所以要签名一致则该修饰函数也会有
一个类似self的参数，从而能够访问类的属性等。

参考博客链接：
http://blog.apcelent.com/python-decorator-tutorial-with-example.html

'''


def testTest():
    test(1, 2, 3)
    test(1, 2, 3)
    m = test(1, 2, 3)
    print m

if __name__ == "__main__":
    testTest()