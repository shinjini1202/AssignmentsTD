import math

num=float(input("Enter a number: "))
if (num<0):
    print("Enter valid number and retry")
else:
    root=math.sqrt(num)
    log=math.log(num)
    sine=math.sin(num)
    print(f"Square root:{root}")
    print(f"Logarithm:{log}")
    print(f"Sine:{sine}")
