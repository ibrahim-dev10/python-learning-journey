ep1 = {123: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566:90}

ep1.update(ep2)
ep1.clear
empt = {}
print(empt)
ep1.pop(123)
ep1.popitem()
print(ep1)


# update() method
info = {'name':'karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)