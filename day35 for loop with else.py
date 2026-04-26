for i in range(6):
    print(i)
    if i== 4:
        break

else:
    print("Sorry no i")    


# what if i change to whilelopp
i = 0
while i<7:
    print(i)
    i = i + 1
    # if i == 4:
    #     break
else:
    print("Sorry no i")       



for x in range(5):
    print("itration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of loop")            