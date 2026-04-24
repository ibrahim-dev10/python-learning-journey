dic = {
    344: "ibrahim",
    65 : "adeel",
    687 : "misbah",
    5435 : "murtaza"

}

print(dic[687])

info = {'name':'karan','age':19, 'eligible':True}
print(info)

# #assessing dictionary items:
# 1.Assessing single value

info = {'name':'karan','age':19, 'eligible':True}
print(info)
# print(info['name2'])
print(info.get('name2'))

# 2.Assessing multipe value
info = {'name':'karan', 'age':19, 'eligible':True}
print(info)
print(info.keys())
print(info.values())
for key in info.keys():
     print(f"The vlaue corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value correspoding to the key {key}is {value}")