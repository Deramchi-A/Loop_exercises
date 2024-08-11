list_numbers=[]
for i in range(1,int(input('Enter your number: '))+1):
    list_numbers.append(i)
sum =sum(list_numbers)
print (list_numbers)
print (sum)
'''
#using for loop and rang function
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)
using built in sum() function
n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)
'''