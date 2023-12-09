#Q10. Given a list [4,2,-3,1,6].
# Write a python program to find if 
# there is a sub-list with sum equal to zero ?

def is_sub_lst_sum_zero (lst) :
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    for k in sublists :
        if sum(k) == 0 :
            return ("Yes, the list has a sub-list with sum equal to zero:",k )
    return ("No, the list has no sub-list with sum equal to zero ")

lst = [4,2,-3,1,6]
result = is_sub_lst_sum_zero(lst)
print(result)
