def height_checker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    heights_sorted = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights_sorted[i] != heights[i]:
            count += 1
    return count


heights = [1, 1, 4, 2, 1, 3]
heights_2 = [5, 1, 2, 3, 4]
heights_3 = [1, 2, 3, 4, 5]

print(height_checker(heights))  # 3
print(height_checker(heights_2))  # 5
print(height_checker(heights_3))  # 0
