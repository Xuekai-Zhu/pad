def solution():
    
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 12

    # Calculate the total number of slices
    total_slices = 4 * SLICES_PER_PIZZA

    # Calculate the number of slices eaten by Bryce and 2 friends
    slices_eaten_by_bryce = (2/3) * SLICES_PER_PIZZA

    # Calculate the number of slices eaten by the two remaining friends
    slices_eaten_by_friends = (2/3) * SLICES_PER_PIZZA

    # Calculate the number of slices left
    slices_left = total_slices - slices_eaten_by_friends - slices_eaten_by_friends

    # Display the number of slices left
    result = slices_left
    return result

print(solution())