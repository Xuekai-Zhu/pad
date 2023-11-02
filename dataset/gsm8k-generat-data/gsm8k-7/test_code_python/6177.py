def solution():
    num_brownies = 16

    # Calculate the number of brownies eaten by Lorraine's children
    num_children_brownies = num_brownies * 0.25

    # Calculate the number of brownies remaining after the children ate
    remaining_brownies = num_brownies - num_children_brownies

    # Calculate the number of brownies eaten by the family for dinner
    num_family_brownies = remaining_brownies * 0.5

    # Calculate the number of brownies remaining after dinner
    remaining_brownies -= num_family_brownies

    # Add the brownie that Lorraine ate before going to bed
    remaining_brownies -= 1

    result = remaining_brownies
    return result

print(solution())