def mergeSortedArrays(arr1,arr2):
    mergedArr = []
    if len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1
    arr1Item = arr1[0]
    arr2Item = arr2[0]
    while len(arr1) != 0 or len(arr2) != 0:
        if len(arr1) != 0:
            arr1Item = arr1[0]
        if len(arr2) != 0:
            arr2Item = arr2[0]
        if len(arr2) == 0 or (arr1Item <= arr2Item):
            mergedArr.append(arr1Item)
            arr1.pop(0)
        elif len(arr1) == 0 or (arr2Item <= arr1Item):
            mergedArr.append(arr2Item)
            arr2.pop(0)

    return mergedArr

print(mergeSortedArrays([0,3,4,31],[4,6,30]))