
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
for i in range(25,50):
   test=is_prime(i)
   if test==True:
       print ("the number (",i,") is prime number")
