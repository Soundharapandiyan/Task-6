#Q3.Given a python list[10,501,22,37,100,999,87,351].
# Find out how many numbers are there in the given Python List which are Happy Numbers ?

def is_happy_num(lst) :
    happy_num = []
    for num in lst:
        temp_dig_sq = set()
        dig_sq = 0
        while num not in temp_dig_sq and dig_sq not in temp_dig_sq and num !=1 and dig_sq != 1:
            temp_dig_sq.add(num)
            dig_sq = sum(int(dig)**2 for dig in str(num))
            if dig_sq == 1 :
                happy_num.append(num)
    return happy_num
lst = [10, 501, 22, 37, 100, 999, 87, 351]
result = is_happy_num(lst)
count_of_happy_numbers = len(result)
print("Count of Happy Numbers:", count_of_happy_numbers)
print("Happy Numbers are in list:", result)

