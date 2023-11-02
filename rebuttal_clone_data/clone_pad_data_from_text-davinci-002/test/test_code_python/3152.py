def solution():
    blue_apples = 5
    yellow_apples = 2 * blue_apples
    total_apples = blue_apples + yellow_apples
    my_son_apples = total_apples / 5
    my_apples = total_apples - my_son_apples
    result = my_apples
    return result

print(solution())