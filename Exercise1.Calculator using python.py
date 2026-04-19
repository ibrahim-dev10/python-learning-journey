num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

print("\n ----Calculator result---")

print(f"Addition:       {num1}  + {num2} = {num1 + num2}")
print(f"Subtraction:    {num1}  - {num2} = {num1 - num2}")
print(f"Multiplication:  {num1} *  {num2} = {num1 * num2}")

if num2!=0:
    print(f"Division:    {num1} /  {num2} = {num1 / num2}")
else:
    print("Division:   cannot be divided by zero!")
    print("programe finish")