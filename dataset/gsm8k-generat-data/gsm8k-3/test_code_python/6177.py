def solution():
    """Lorraine made a pan of brownies and cut them into 16 pieces.  Her children ate 25% of the brownies when they got home from school.  After dinner,  the entire family ate 50% of the remaining brownies.  After everyone went to bed, Lorraine ate 1 more brownie.  How many brownies are left over?"""
    # Define the initial number of brownie pieces
    initial_brownies = 16

    # Calculate the number of brownie pieces eaten by the children
    children_brownies = initial_brownies * 0.25

    # Calculate the number of brownie pieces remaining after the children eat
    remaining_brownies = initial_brownies - children_brownies

    # Calculate the number of brownie pieces eaten by the family after dinner
    family_brownies = remaining_brownies * 0.5

    # Calculate the number of brownie pieces remaining after the family eats
    remaining_brownies -= family_brownies

    # Calculate the final number of brownies after Lorraine eats one more
    final_brownies = remaining_brownies - 1

    # Display the final number of brownies
    result = final_brownies
    return result

print(solution())