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
        def wra(*args, **kwargs):
            result = inputFunc(*args, **kwargs)
            return result

        return wra
    return innerFunction


@wraper(1,2)
def test(*args, **kwargs):
    print 'test'

'''
根据对这里的代码的理解，使用functools的wraps时只有该修饰符号后定义的函数才需要与被修饰的函数的函数签
一样。
而且感觉method修饰和函数修饰没什么区别，因为method修饰是对类的方法进行修饰，所以要签名一致则该修饰函数也会有
一个类似self的参数，从而能够访问类的属性等。
参考博客链接：
http://blog.apcelent.com/python-decorator-tutorial-with-example.html

'''

if __name__ == "__main__":
    test(1,2,3)