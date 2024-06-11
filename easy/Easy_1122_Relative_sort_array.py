def relative_sort_array(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    if len(arr1) == len(arr2):
        return arr2
    f = s = 0
    result = []
    while s < len(arr2):
        if arr1[f] == arr2[s]:
            result.append(arr1.pop(f))
        else:
            if f == len(arr1) - 1:
                f = 0
                s += 1
            else:
                f += 1
    for i in sorted(arr1):
        result.append(i)
    return result


arr11 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr12 = [2, 1, 4, 3, 9, 6]

arr21 = [28, 6, 22, 8, 44, 17]
arr22 = [22, 28, 8, 6]

arr31 = [943, 790, 427, 722, 860, 550, 225, 846, 715, 320]
arr32 = [943, 715, 427, 790, 860, 722, 225, 320, 846, 550]

print(relative_sort_array(arr11, arr12))  # [2,2,2,1,4,3,3,9,6,7,19]
print(relative_sort_array(arr21, arr22))  # [22,28,8,6,17,44]
print(relative_sort_array(arr31, arr32))  # [943, 715, 427, 790, 860, 722, 225, 320, 846, 550]
