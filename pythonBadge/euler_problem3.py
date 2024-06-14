import math


factor = 2

def is_prime(n):
    square_root = math.sqrt(n)
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor <= square_root and n % divisor != 0:
        divisor += 2
    return divisor > square_root


    

num = 600851475143
result = 2
#while num > 1:
for i in range(round(math.sqrt(num))):
    if is_prime(i):

        if num % i == 0:
            result = i
            
                
print(result)