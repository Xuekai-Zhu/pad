def solution():
    num_brownies = 16  # Lorraine made a pan of brownies and cut them into 16 pieces

    # Calculate the number of brownies eaten by the children
    num_children_brownies = num_brownies * 0.25

    # Calculate the remaining brownies after the children ate
    remaining_brownies = num_brownies - num_children_brownies

    # Calculate the number of brownies eaten after dinner
    num_dinner_brownies = remaining_brownies * 0.5

    # Calculate the remaining brownies after dinner
    remaining_brownies = remaining_brownies - num_dinner_brownies

    # Calculate the remaining brownies after Lorraine ate one more
    remaining_brownies -= 1

    result = remaining_brownies
    return result

print(solution())