#Factorial number:
number= int(input("Enter the number you want to factor: "))
res=1
for i in range (1,number+1):
    res=res *i
print (res)
   

'''
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
'''