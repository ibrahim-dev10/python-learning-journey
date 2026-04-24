s1 = {1,2,4,5,9}
s2 = {5,9,8}
print(s1.union(s2))
s1.update(s2)
print(s1.s2)

#UNION
cities = {"Tokyo", "Madrid", "Berlin","Dehli"}
cities2 = {"Tokyo", "Seaoul","Kabul","Madrid"}
cities3 = cities.union(cities2)
print(cities3)

#INTERSECTION
cities = {"Tokyo", "Madrid", "Berlin","Dehli"}
cities2 = {"Tokyo", "Seaoul", "Kabul","Madrid"}
cities.intersection_update(cities2)
print(cities)

#SYMMETRIC DIFFERENCE
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seaoul","Kabul"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)