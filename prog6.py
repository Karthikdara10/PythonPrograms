#indexing on str
>>> x="python programming"
>>> print(x,type(x),id(x))
python programming <class 'str'> 2894582841456
>>> len(x)
18
>>> x[0]
'p'
>>> x[1]
'y'
>>> x[2]
't'
>>> x[3]
'h'
>>> x[19]
IndexError: string index out of range

#slicing on str
>>> x="python programming"
>>> print(x,type(x),id(x))
python programming <class 'str'> 2894582856752
>>> len(x)
18
>>> x[0:18]
'python programming'
>>> x[::-1]
'gnimmargorp nohtyp'
>>> x[0:9]
'python pr'
>>> x[-1:-10]
''
>>> x[1:5]
'ytho'
>>> x[9:13]
'ogra'