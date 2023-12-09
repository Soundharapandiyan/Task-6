#Q4. Write a python program to find the sum of the first and last digit of an integer ?
def sum_1st_last (num) :
    sum = int(num[0]) + int(num[-1])
    return sum
num = input("Enter the integer : ")
result = sum_1st_last(num)
print("Sum of the first and last digit:",result)