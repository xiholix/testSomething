#--*--coding:utf8--*--
#File: setup.py
#! /home/xie/anaconda2/bin/python
from distutils.core import setup, Extension

#生成一个扩展模块
pht_module = Extension('_helloworld', #模块名称，必须要有下划线
                        sources=['helloworld_wrap.cxx', #封装后的接口cxx文件
                                 'helloworld.cpp'  #此处一定要把原始的cpp文件也包括,否则会报错
                                ],
                      )

setup(name = 'helloworld',	#打包后的名称
        version = '0.1',
        author = 'SWIG Docs',
        description = 'Simple swig pht from docs',
        ext_modules = [pht_module], #与上面的扩展模块名称一致
        py_modules = ['helloworld'], #需要打包的模块列表
    )
