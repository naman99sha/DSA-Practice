# O(nlogn)

# Needs a helper Pivot function
def pivot(arr,pivotIdx,endIdx):
    swapIdx = pivotIdx
    for i in range(pivotIdx+1, endIdx+1):
        if arr[i] < arr[pivotIdx]:
            swapIdx += 1
            arr[swapIdx],arr[i] = arr[i],arr[swapIdx]
    arr[pivotIdx],arr[swapIdx] = arr[swapIdx],arr[pivotIdx]
    return swapIdx

def quickSort(arr,left,right):
    if left < right:
        pivotIdx = pivot(arr,left,right)
        quickSort(arr,left,pivotIdx-1)
        quickSort(arr,pivotIdx+1,right)
    return arr
    
print(quickSort([4,6,1,7,3,2,5],0,6))

