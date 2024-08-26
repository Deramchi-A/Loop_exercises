#reversed number
number=input("Enter the number you want to reverse: ")
length_number=len(number)
print(number[length_number::-1])

'''
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)
'''