def average(a, b, c=1):
    print("The average is ", (a + b + c) /2)



def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
     sum = sum + 1
    print("Average is: " , sum / len(numbers))
    # return 7
    return sum / len(numbers)

# average(4,6)    
# average(b=9)

# def name(fname, mname = "john", lname = "whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy", "Agrwal", "Jain")    


# keyword argument
# average(b=9, a=21)

# required argument
c = average(5, 6 , 7, 1)
print(c)


# example
# def name(fname, lname, mname=""):
#     print("Hello," , fname, mname, lname)

# name("Peter", "Quill")


