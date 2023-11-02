def solution():
    """Lorraine made a pan of brownies and cut them into 16 pieces. Her children ate 25% of the brownies when they got home from school. After dinner, the entire family ate 50% of the remaining brownies. After everyone went to bed, Lorraine ate 1 more brownie. How many brownies are left over?"""
    # Define the initial number of brownies
    initial_brownies = 16

    # Calculate the number of brownies eaten by the children
    children_brownies = initial_brownies * 0.25

    # Calculate the number of brownies remaining after the children have eaten
    remaining_brownies = initial_brownies - children_brownies

    # Calculate the number of brownies eaten by the family after dinner
    family_brownies = remaining_brownies * 0.5

    # Calculate the total number of brownies eaten
    total_brownies_eaten = children_brownies + family_brownies + 1

    # Calculate the number of brownies left over
    left_over_brownies = initial_brownies - total_brownies_eaten

    # return the result
    result = left_over_brownies
    return result

print(solution())