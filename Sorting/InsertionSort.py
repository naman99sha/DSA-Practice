def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j -= 1
    return arr

print(insertionSort([99,44,6,2,1,5,63,87,283,4,0]))
