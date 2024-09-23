>>> lst=[100,2.2,True,2+3j,"python"]
>>> print(lst,type(lst),id(lst))
[100, 2.2, True, (2+3j), 'python'] <class 'list'> 2894584272128
***********************************************************
Pre Defined Functions In List
***********************************************************
1.append(insert the value at last)
***********
>>> lst=[10,20,30,40]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40] <class 'list'> 2894582813568
>>> lst.append(25)
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 25] <class 'list'> 289458281356
2.insert(based on the indexing)
***********
>>> lst=[10,20,30,40]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40] <class 'list'> 2894584272128
>>> lst.insert(1,15)
>>> print(lst,type(lst),id(lst))
[10, 15, 20, 30, 40] <class 'list'> 2894584272128
***********************************************************
3.clear(clear the list)
**********
>>> lst=[10,20,30,40]
>>> print(lst,type(lst),id(lst))
>>> lst.clear()
>>> print(lst,type(lst),id(lst))
[] <class 'list'> 2894582813568
***********************************************************
4.remove(based on value)
***********
>>> lst=[10,20,30,40,50]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50] <class 'list'> 2894584272128
>>> lst.remove(20)
>>> print(lst,type(lst),id(lst))
[10, 30, 40, 50] <class 'list'> 2894584272128
>>> lst.remove(10)
>>> print(lst,type(lst),id(lst))
[30, 40, 50] <class 'list'> 2894584272128
***********************************************************
5.pop(index)
*************
>>> lst=[10,20,30,40,50]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50] <class 'list'> 2894582813568
>>> lst.pop(0)
10
>>> print(lst,type(lst),id(lst))
[20, 30, 40, 50] <class 'list'> 2894582813568
>>> lst.pop(1)
30
>>> print(lst,type(lst),id(lst))
[20, 40, 50] <class 'list'> 2894582813568
***********************************************************
6.pop()
********
>>> lst=[10,20,30,40,50]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50] <class 'list'> 2894584272128
>>> lst.pop()
50
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40] <class 'list'> 2894584272128
>>> lst.pop()
40
>>> print(lst,type(lst),id(lst))
[10, 20, 30] <class 'list'> 2894584272128
>>> lst.pop()
30
>>> print(lst,type(lst),id(lst))
[10, 20] <class 'list'> 2894584272128
***********************************************************
7.index()
**********
>>> lst=[10,20,30,40,50]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50] <class 'list'> 2894582813568
>>> lst.index(50)
4
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50] <class 'list'> 2894582813568
>>> lst.index(40)
3
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50] <class 'list'> 2894582813568
>>>
***********************************************************
8.copy()
*********
>>> lst1=[10,20,30]
>>> print(lst1,type(lst1),id(lst1))
[10, 20, 30] <class 'list'> 2894582813568
>>> lst2=lst1.copy()
>>> print(lst2,type(lst2),id(lst2))
[10, 20, 30] <class 'list'> 2894580119936
>>> lst2
[10, 20, 30]
>>> lst1
[10, 20, 30]
>>>
***********************************************************
9.count()
**********
>>> lst=[10,20,30,40,50,10,20]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50, 10, 20] <class 'list'> 2894584272128
>>> lst.count(10)
2
>>> lst.count(20)
2
>>>
***********************************************************
10.reverse()
*************
>>> lst1=[10,20,30,40,50]
>>> print(lst1,type(lst1),id(lst1))
[10, 20, 30, 40, 50] <class 'list'> 2894584269888
>>> lst2.reverse()
>>> print(lst2,type(lst2),id(lst2))
[30, 20, 10] <class 'list'> 2894580119936
>>>
***********************************************************
11.sort()
**********
>>> lst=[10,20,30,40,50,60]
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50, 60] <class 'list'> 2894582813568
>>> lst.sort()
>>> print(lst,type(lst),id(lst))
[10, 20, 30, 40, 50, 60] <class 'list'> 2894582813568
>>> lst.sort(reverse=True)
>>> print(lst,type(lst),id(lst))
[60, 50, 40, 30, 20, 10] <class 'list'> 2894582813568
>>>
***********************************************************