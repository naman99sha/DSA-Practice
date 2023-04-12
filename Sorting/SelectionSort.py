def selectionSort(arr):
    temp = 0
    while (temp < len(arr)):
        smallest = None
        smallestIdx = None
        for i in range(temp,len(arr)):
            if smallest == None:
                smallest = arr[i]
                smallestIdx = i
            elif arr[i] < smallest:
                smallest = min(smallest,arr[i])
                smallestIdx = i
        arr[temp],arr[smallestIdx] = arr[smallestIdx],arr[temp]
        temp += 1
    return arr

print(selectionSort([99,44,6,2,1,5,63,87,283,4,0]))