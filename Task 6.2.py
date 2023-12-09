# 2. Given a python list[10,501,22,37,100,999,87,351] 
# your task is to count all the Prime Numbers and
# create a new python list which will contain all the Prime Numbers in it ?

def prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
original_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in original_list if prime(num)]
count_of_primes_numbers= len(prime_numbers)

print("Count of Prime Numbers:", count_of_primes_numbers)
print("Prime Numbers:", prime_numbers)