def solution():
    num_of_tomatoes = 100
    picked_tomatoes = num_of_tomatoes * (1/4)
    tomatoes_left = num_of_tomatoes - picked_tomatoes
    tomatoes_left -= 20
    tomatoes_left -= (picked_tomatoes * 2)

    result = tomatoes_left
    return result

print(solution())