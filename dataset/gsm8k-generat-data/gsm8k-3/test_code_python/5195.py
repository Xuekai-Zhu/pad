def solution():
    """Era had 5 burgers for her and her 4 friends. She sliced each burger into halves. The first and second friends got 1 and 2 slices, respectively. Then the third and fourth friends got 3 slices each. How many slices of burgers are left for Era?"""
    # Define the number of burgers and slices per burger
    burgers = 5
    slices_per_burger = 2

    # Calculate the total number of slices
    total_slices = burgers * slices_per_burger

    # Subtract the slices given to the friends
    total_slices -= 1 + 2 + 3 + 3

    # Display the remaining slices for Era
    result = total_slices
    return result

print(solution())