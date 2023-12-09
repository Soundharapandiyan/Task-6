#Q7. Write a python program to find the first
# non-repeating elements in a given list of integers ?

def first_non_rep(lst) :
    count_dict = {}
    for num in lst :
        if num not in count_dict :
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    for num1 in lst:
        if count_dict[num1] == 1 :
            return num1
    return ("No repeating elements")

lst = [15,13,17,29,46,13,18,15]
result = first_non_rep(lst)
print("First non repeating element is : ",result)

