#Q6. You have been given three lists. 
# Your task is to find the duplicates in the thre lists. 
# Wite a python program for the same
# You can use your own python lists?

list1 = list(input("Enter list 1 elements seperated by space : ").split())
list2 = list(input("Enter list 1 elements seperated by space : ").split())
list3 = list(input("Enter list 1 elements seperated by space : ").split())
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
common_elements = set1.intersection(set2, set3)
duplicates = list(common_elements)
print("The duplicate elements in three lists are : ", duplicates)
