def solution():
    """Mabel planted 4 tomato plants. One tomato plant bore 8 tomatoes and another bore 4 more tomatoes than the first. The two remaining plants each bore three times the number of tomatoes as the first two plants combined. How many tomatoes does Mabel have?"""
    # Define the number of tomatoes on the first plant
    tomatoes_1 = 8

    # Calculate the number of tomatoes on the second plant
    tomatoes_2 = tomatoes_1 + 4

    # Calculate the total number of tomatoes on the first two plants
    total_1_2 = tomatoes_1 + tomatoes_2

    # Calculate the number of tomatoes on each of the remaining two plants
    tomatoes_3 = 3 * total_1_2
    tomatoes_4 = 3 * total_1_2

    # Calculate the total number of tomatoes
    total_tomatoes = tomatoes_1 + tomatoes_2 + tomatoes_3 + tomatoes_4

    # Display the total number of tomatoes
    result = total_tomatoes
    return result

print(solution())