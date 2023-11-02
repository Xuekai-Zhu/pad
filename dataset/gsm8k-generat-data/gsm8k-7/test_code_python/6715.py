def solution():
    c_first_throw = 20
    j_first_throw = c_first_throw - 4
    c_second_throw = c_first_throw + 10
    j_second_throw = j_first_throw * 2
    c_third_throw = c_second_throw + 4
    j_third_throw = c_first_throw + 17

    # Find the maximum height thrown among all six throws
    max_height = max(c_first_throw, j_first_throw, c_second_throw,
                     j_second_throw, c_third_throw, j_third_throw)
    result = max_height
    return result

print(solution())