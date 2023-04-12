# Breaks down the list in halves and keeps doing it until single length lists remain.
# Then combines 2 lists at a time and sorts them
# Will need a helper function to merge/combine the lists
# O(nlogn)

# Helper Function
def merge(lst1, lst2):
    i = 0
    j = 0
    temp = []
    while i<len(lst1) and j<len(lst2):
        if lst1[i] < lst2[j]:
            temp.append(lst1[i])
            i += 1
        elif lst1[i] >= lst2[j]:
            temp.append(lst2[j])
            j += 1
    while i < len(lst1):
        temp.append(lst1[i])
        i+=1
    while j < len(lst2):
        temp.append(lst2[j])
        j+=1
    return temp

# Function for breaking the array in halves and calling the helper function
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

print(mergeSort([9,1,7,2]))