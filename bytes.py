#byte is used to implement end-to-end encryption
>>> x=[10,20,30,40,50,60]
>>> print(x,type(x))
[10, 20, 30, 40, 50, 60] <class 'list'>
>>> b=bytes(x)
>>> print(b,type(b))
b'\n\x14\x1e(2<' <class 'bytes'>

#indexing on list
>>> b[0]
10
>>> b[1]
20
>>> b[2]
30