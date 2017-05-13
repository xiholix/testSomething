//File: helloworld.i
%module helloworld

%{
#define SWIG_FILE_WITH_INIT
#include "helloworld.h"
%}

%include "helloworld.h"
