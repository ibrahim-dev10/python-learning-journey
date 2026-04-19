#String are immutable
a = "!!!Ibrahim!!!!! !!!! Ibrahim"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Ibrahim", "john"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Ibrahim"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Den. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))


str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())