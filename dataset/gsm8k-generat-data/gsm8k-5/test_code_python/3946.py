def solution():
    initial_brownies = 2 * 12  # Mother made 2 dozen brownies initially
    eaten_by_father = 8  # Father ate 8 of the brownies
    eaten_by_daughter = 4  # Daughter ate 4 of the brownies
    remaining_brownies = initial_brownies - eaten_by_father - eaten_by_daughter  # Calculate remaining brownies

    # Add the second batch of brownies
    new_brownies = 2 * 12 
    total_brownies = remaining_brownies + new_brownies  # Calculate total brownies on the counter
    result = total_brownies
    return result

print(solution())