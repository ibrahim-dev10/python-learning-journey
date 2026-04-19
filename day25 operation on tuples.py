countries = ("Spain", "Italy", "India","England","Germany")
temp =  list(countries)
temp.append("Russia")      #add item
temp.pop(3)                #remove item
temp[2] = "Finland"        #change item
countries = tuple(temp)
print(countries)


countries = ("Pakistan","Afghanistan", "Bangladesh","Shrlinka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#Tuple methods
# count()method

tuple1 = (0,1,2,3,4,5,6,7,8,3,45,68,3,45,3)
res = tuple1.count(3)
print("count of 3 in tuple1 is:", res)


#Index method
tuple1 = (0,1,2,31,2,3,1,3,2,3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
print("count of 3 in tuple1 is:", res)
