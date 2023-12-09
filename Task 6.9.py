#Q9. You have been given a python list[10,20,30,9] and a value of 59.
# Write a python program to find the triplet in
# the list whose sum is equal to the given value ?

def find_triplets(lst, triplet_sum):
    n = len(lst)
    triplets = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == triplet_sum:
                    triplets.append([lst[i], lst[j], lst[k]])

    return triplets

lst = [10, 20, 30, 9]
triplet_sum = 59

triplets = find_triplets(lst, triplet_sum)

if triplets:
    print("Triplets are :")
    for triplet in triplets:
        print(triplet)
else:
    print("There are no triplets ")

