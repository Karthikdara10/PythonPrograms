>>> x=(100,2.32,True,2+3j,"Python")
>>> print(x,type(x))
(100, 2.32, True, (2+3j), 'Python') <class 'tuple'>
>>> x.count(100)
1
>>> x.index(100)
0
>>> x=(10,"python",10,20,30,50,20,10,2+3j,False)
>>> print(x,type(x))
(10, 'python', 10, 20, 30, 50, 20, 10, (2+3j), False) <class 'tuple'>
>>> x.count(10)
3
>>> x.index(False)
9
