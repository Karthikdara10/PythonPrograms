#Type casting techniques--- int(float/bool/complex/str)
>>> x=2.32
>>> print(x,type(x))
2.32 <class 'float'>
>>> y=int(x)
>>> print(y,type(y))
2 <class 'int'>
**************************
>>> x=True
>>> print(x,type(x))
True <class 'bool'>
>>> y=int(x)
>>> print(y,type(y))
1 <class 'int'>
**************************
>>> x=2+3j
>>> print(x,type(x))
(2+3j) <class 'complex'>
>>> y=int(x)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

>>> x=2+3j
>>> print(x,type(x))
(2+3j) <class 'complex'>
>>> y=int(x.real)
>>> print(y,type(y))
2 <class 'int'>
**************************
>>> x="karthik"
>>> print(x,type(x))
karthik <class 'str'>
>>> y=int(x)
ValueError: invalid literal for int() with base 10: 'karthik'
**************************
>>> x="12"
>>> print(x,type(x))
12 <class 'str'>
>>> y=int(x)
12 <class 'int'>
****************************************************************************************************************
#Type casting techniques--- float(int,complex,bool,,str)
>>> x=100
>>> print(x,type(x))
100 <class 'int'>
>>> f=float(x)
>>> print(f,type(f))
100.0 <class 'float'>
**************************
>>> x=2+3j
>>> print(x,type(x))
(2+3j) <class 'complex'>
>>> f=float(x.imag)
>>> print(f,type(f))
3.0 <class 'float'>
>>> f=float(x.real)
>>> print(f,type(f))
2.0 <class 'float'>
**************************
>>> x=False
>>> print(x,type(x))
False <class 'bool'>
>>> f=float(x)
>>> print(f,type(f))
0.0 <class 'float'>
**************************
>>> x="12"
>>> print(x,type(x))
12 <class 'str'>
>>> f=float(x)
>>> print(f,type(f))
12.0 <class 'float'>
****************************************************************************************************************
#Type casting techniques--- bool(int,float,complex,str)
>>> x=100
>>> print(x,type(x))
100 <class 'int'>
>>> b=bool(x)
>>> print(b,type(b))
True <class 'bool'>
>>> x=-12
>>> print(x,type(x))
-12 <class 'int'>
>>> b=bool(x)
>>> print(b,type(b))
True <class 'bool'>
>>> b=bool(0)
>>> print(b,type(b))
False <class 'bool'>
**************************
>>> x=2.32
>>> print(x,type(x),id(x))
2.32 <class 'float'> 2894579215280
>>> b=bool(x)
>>> print(b,type(b))
True <class 'bool'>
**************************
>>> x=2+3j
>>> print(x,type(x),id(x))
(2+3j) <class 'complex'> 2894582710768
>>> b=bool(x)
>>> print(b,type(b))
True <class 'bool'>
**************************
>>> x="karthik"
>>> print(x,type(x),id(x))
karthik <class 'str'> 2894582825440
>>> b=bool(x)
>>> print(b,type(b))
True <class 'bool'>
****************************************************************************************************************
#Type casting techniques---complex(int,float,bool,str)
>>> x=100
>>> print(x,type(x),id(x))
100 <class 'int'> 140731038242328
>>> c=complex(x)
>>> print(c,type(c))
(100+0j) <class 'complex'>
**************************
>>> x=2.32
>>> print(x,type(x),id(x))
2.32 <class 'float'> 2894582711824
>>> c=complex(x)
>>> print(c,type(c))
(2.32+0j) <class 'complex'>
**************************
>>> x=True
>>> print(x,type(x),id(x))
True <class 'bool'> 140731037438480
>>> c=complex(x)
>>> print(c,type(c))
(1+0j) <class 'complex'>
**************************
>>> x="karthik"
>>> print(x,type(x),id(x))
karthik <class 'str'> 2894582825440
>>> c=complex(x)
ValueError: complex() arg is a malformed string
**************************
>>> x="12"
>>> print(x,type(x),id(x))
12 <class 'str'> 2894582840800
>>> c=complex(x)
>>> print(c,type(c))
(12+0j) <class 'complex'>
****************************************************************************************************************
#Type casting techniques---str(int,float,bool,complex,)
>>> x=100
>>> print(x,type(x),id(x))
100 <class 'int'> 140731038242328
>>> s=str(x)
>>> print(s,type(s),id(s))
100 <class 'str'> 2894582832400
**************************
>>> x=3.47
>>> print(x,type(x),id(x))
3.47 <class 'float'> 2894579215280
>>> s=str(x)
>>> print(s,type(s),id(s))
3.47 <class 'str'> 2894582827216
**************************
>>> x=False
>>> print(x,type(x),id(x))
False <class 'bool'> 140731037438512
>>> s=str(x)
>>> print(s,type(s),id(s))
False <class 'str'> 140731038261168
**************************
>>> x=2+3j
>>> print(x,type(x),id(x))
(2+3j) <class 'complex'> 2894582726512
>>> s=str(x)
>>> print(s,type(s),id(s))
(2+3j) <class 'str'> 2894582827216
**************************
>>> x="karthik"
>>> print(x,type(x),id(x))
karthik <class 'str'> 2894582825440
>>> s=str(x)
>>> print(s,type(s),id(s))
karthik <class 'str'> 2894582825440
****************************************************************************************************************
