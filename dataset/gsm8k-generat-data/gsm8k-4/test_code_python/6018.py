def solution():
    """Katy makes some brownies to eat throughout the week. She eats 5 on Monday and twice as many on Tuesday. After she has eaten the brownies on Tuesday, all of the brownies she made are gone. How many brownies did Katy make?"""
    # Define the number of brownies eaten on Monday
    monday_brownies = 5

    # Define the number of brownies eaten on Tuesday
    tuesday_brownies = monday_brownies * 2

    # Define the total number of brownies made
    total_brownies = monday_brownies + tuesday_brownies

    # Return the result
    result = total_brownies
    return result

print(solution())