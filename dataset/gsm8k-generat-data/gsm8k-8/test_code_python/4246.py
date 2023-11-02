def solution():
    # Calculate the number of tomatoes on the first two plants
    tomatoes_on_first = 8
    tomatoes_on_second = tomatoes_on_first + 4
    total_tomatoes_on_first_two = tomatoes_on_first + tomatoes_on_second

    # Calculate the number of tomatoes on the last two plants
    tomatoes_on_third = 3 * total_tomatoes_on_first_two
    tomatoes_on_fourth = 3 * total_tomatoes_on_first_two

    # Calculate the total number of tomatoes
    total_tomatoes = tomatoes_on_first + tomatoes_on_second + tomatoes_on_third + tomatoes_on_fourth
    result = total_tomatoes
    return result

print(solution())