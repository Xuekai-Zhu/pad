def solution():
    """Mabel planted 4 tomato plants. One tomato plant bore 8 tomatoes and another bore 4 more tomatoes than the first. The two remaining plants each bore three times the number of tomatoes as the first two plants combined. How many tomatoes does Mabel have?"""
    # Calculate the number of tomatoes on the first two plants
    tomatoes_first_two = 8 + (8+4)

    # Calculate the total number of tomatoes on the remaining two plants
    tomatoes_remaining = 3 * tomatoes_first_two

    # Calculate the total number of tomatoes
    total_tomatoes = tomatoes_first_two + tomatoes_remaining

    result = total_tomatoes
    return result

print(solution())