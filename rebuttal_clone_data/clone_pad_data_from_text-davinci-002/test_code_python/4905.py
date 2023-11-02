def solution():
    jar_size = 100
    big_toenails = 20
    regular_toenails = 40
    size_of_big_toenails = 2
    size_of_regular_toenails = 1
    remaining_space = jar_size - (big_toenails * size_of_big_toenails + regular_toenails * size_of_regular_toenails)
    result = remaining_space / size_of_regular_toenails
    return result

print(solution())