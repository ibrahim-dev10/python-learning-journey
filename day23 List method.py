num = [1, 2, 3, 4, 6] #Ex1
num.sort()
print(num)


l = [1, 2, 3, 4] #Ex2
print(l)
l.append(7)
print(l)


l = [11, 45, 1, 2, 3, 4, 6] #Ex3 Assending Order
print(l)
l.sort()
print(l)


l = [11, 45, 1, 2, 3, 4, 6] #Ex4 Desending Order
print(l)
l.sort(reverse = True)
print(l)


l = [6, 4, 2, 1, 45, 11] #Ex5
print(l)
l.reverse()
print(l)

#Index
l = [6, 4, 2, 1, 45, 11, 1]
print(l.index(1))


#count
l = [1,2,3,4,1]
print(l.count(1))


#copyfunction
l = [2, 3, 6, 7]
m = l.copy()
m[0] = 0
print(l)


#insert
l = [11, 2, 44, 55, 78]
l.insert(1, 899)
print(l)

#Extend
l = [11, 34, 76, 98]#concating of two list
m = [900, 100, 1100]
k = l + m
l.extend(m)
print(l)


