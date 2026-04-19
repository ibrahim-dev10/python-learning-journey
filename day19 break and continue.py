for i in range(12):
    if(i == 10):
        break
    print("5 x", i+1, "=" , 5 * (i+1))


print("Loop ko chodkar nikal gaya")    


for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 x" , i, "=", 5 * i)

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break