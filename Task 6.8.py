#Q8.Write a python program to 
# find the minimum element in a rated and sorted list ?

def find_min_ele (lst) :
    sorted_lst = sorted(lst)
    return sorted_lst[0]
lst = [15,13,17,29,46,13,18,15]
result = find_min_ele(lst)
print("minimum element is : ",result)
