def solution():
    """Phil and Andre decide to order some pizza. They get a small cheese and a large pepperoni. The small pizza has 8 slices, The large has 14 slices. They have both eaten 9 slices already. How many pieces are left per person?"""
    # Define the number of slices in each pizza
    SMALL_PIZZA_SLICES = 8
    LARGE_PIZZA_SLICES = 14

    # Define the number of slices already eaten
    slices_eaten = 9

    # Calculate the total number of slices left
    total_slices_left = (SMALL_PIZZA_SLICES + LARGE_PIZZA_SLICES) - (slices_eaten * 2)

    # Calculate the number of slices left per person
    slices_left_per_person = total_slices_left / 2

    # Display the number of slices left per person
    result = slices_left_per_person
    
    return result

print(solution())