def factorial(n):
    if n<0:
        print("Enter valid number")
        return 0
    if n==0:
        return 1
    result=1
    for i in range(1,n+1):
        result *=i
    return result
num=int(input("Enter a number: "))
output=factorial(num)
if (output>0):
    print("Factorial of "+str(num)+" is "+str(output))
