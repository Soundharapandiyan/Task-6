#Q5.You have been given list of N integerhich represents the number of Mangoes in a bag.
#Each bag has a variable number of Mangoes.There are M students in a Guvi class, your task is to distribute the Mangoes 
# in such a way that each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes
#and minimum Mangoes given to the student is minimum ?

def dis_mangoes(lst,M) :
    sorted_lst = sorted(lst)
    distri_to_stu = []
    N = len(lst)
    if N < M :
        return ("Can't distribute to all students")
    else :
        for i in range(M) :
            distri_to_stu.append(sorted_lst[i])
        return distri_to_stu
lst = list(input("Enter the list of number of mangoes in bag seperated by space : ").split())
M = int(input("Enter the number of students : "))
result = " ".join(map(str,dis_mangoes(lst,M)))
print("The distributed bags are : ",result)

