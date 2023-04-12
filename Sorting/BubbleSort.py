def bubbleSort(arr):
    temp = len(arr)
    while temp > 0:
        for j in range(temp-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                continue
        temp -= 1
    return arr

print(bubbleSort([99,44,6,2,1,5,63,87,283,4,0]))