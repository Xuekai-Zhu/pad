def solution():
    brownies_on_monday = 5  # Katy eats 5 brownies on Monday
    brownies_on_tuesday = 2 * brownies_on_monday  # Katy eats twice as many brownies on Tuesday

    # Calculate the total number of brownies Katy eats
    total_brownies = brownies_on_monday + brownies_on_tuesday

    # Calculate the total number of brownies Katy made
    # Since she ate all the brownies she made, the number of brownies she made is equal to the number of brownies she ate
    brownies_made = total_brownies

    result = brownies_made
    return result

print(solution())