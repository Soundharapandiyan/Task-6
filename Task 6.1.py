# 1.You have been given a python list [10,501,22,37,100,999,87,351] 
# your task is to create two list one which have all the Even numbers
# and another list which have all the Odd numbers i it ?

list = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = [num for num in list if num % 2 == 0]
odd_numbers = [num for num in list if num % 2 != 0]
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)