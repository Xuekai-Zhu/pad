def solution():
    """Katy makes some brownies to eat throughout the week. She eats 5 on Monday and twice as many on Tuesday. After she has eaten the brownies on Tuesday, all of the brownies she made are gone. How many brownies did Katy make?"""
    monday_brownies = 5
    tuesday_brownies = 2 * monday_brownies
    total_brownies = monday_brownies + tuesday_brownies
    result = total_brownies
    return result

print(solution())