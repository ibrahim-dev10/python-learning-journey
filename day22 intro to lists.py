marks = [3, 5, 6, "Harry", True, 8, 5, 3, 1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #Negative index
print(marks[len(marks)-3]) #positive index
print(marks[5-3]) #positive index
print(marks[2]) #positive idex

if 7 in marks: #check whether the item is present or not
    print("Yes")
else:
    print("No")

# #Same thing applies for string as well!
if "Ha" in "Harry":
    print("Yes")    

#jumping index
print(marks)
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

#list index
colors = ["Red", "Blue", "Green", "Black"]
print(colors[0])
print(colors[1])
print(colors[2])


