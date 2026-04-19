tup = (1, 5, 764,88999)
print(type(tup), tup)

tup1 = (1,2,3,4,5,6,7) #EX1
tup2 = ("Red", "Green", "Blue")
print(tup1)
print(tup2)
print(tup[0])
print(tup[1])


#Tuple Index
country = ("Spain","Italy","India") #POSITIVE INDEXING
print(country[0])
print(country[1])
print(country[2])

country = ("Spain", "India", "Pakistan", "Iran") #NEGATIVE INDEXING
print(len(country))
print(country[-3])
print(country[-1])

if 88999 in tup: #check for item
    print("Yes 88999 is present in this tuple")