def min_time_to_type(word):
    left = right = 97
    steps = 0
    for letter in word:
        while True:
            if left < 97:
                left = 122
            if right > 122:
                right = 97
            if chr(left) == letter:
                right = left
                break
            if chr(right) == letter:
                left = right
                break
            left -= 1
            right += 1
            steps += 1

    return steps + len(word)


word = "abc"
word_2 = "bza"
word_3 = "zjpc"
print(min_time_to_type(word))  # 5
print(min_time_to_type(word_2))  # 7
print(min_time_to_type(word_3))  # 34
