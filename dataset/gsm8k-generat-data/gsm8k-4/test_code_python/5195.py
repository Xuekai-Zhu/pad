def solution():
    """Era had 5 burgers for her and her 4 friends. She sliced each burger into halves. The first and second friends got 1 and 2 slices, respectively. Then the third and fourth friends got 3 slices each. How many slices of burgers are left for Era?"""
    # Define the number of burgers and slices per burger
    burgers = 5
    slices_per_burger = 2

    # Calculate the total number of slices of burgers
    total_slices = burgers * slices_per_burger

    # Calculate the number of slices given to the first two friends
    first_two_slices = 1 + 2

    # Calculate the number of slices given to the third and fourth friends
    third_fourth_slices = 3 + 3

    # Calculate the total number of slices given to the friends
    total_friend_slices = first_two_slices + third_fourth_slices

    # Calculate the number of slices left for Era
    slices_left = total_slices - total_friend_slices

    # Return the result
    result = slices_left
    return result

print(solution())