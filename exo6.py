#my solution
len_number=int(0)
number="78657"
print(len(number))
while len_number<len(number):
    len_number+=1
print (len_number)
#their solution
num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10
    print(num)
    count+=1
print (count)