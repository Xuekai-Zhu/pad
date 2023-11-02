def solution():
    """Blanch has 15 slices of pizza in the fridge. During breakfast, she eats 4 slices. At lunch, Blanch eats 2 slices, then takes two slices as a snack. Finally, she consumes 5 slices for dinner. How many slices of pizza are left?"""
    # Define the starting number of pizza slices
    starting_slices = 15

    # Calculate the number of slices eaten at each meal
    breakfast_slices = 4
    lunch_slices = 2 + 2
    dinner_slices = 5

    # Calculate the total number of slices eaten
    total_slices_eaten = breakfast_slices + lunch_slices + dinner_slices

    # Calculate the number of slices remaining
    slices_remaining = starting_slices - total_slices_eaten

    # Display the number of slices remaining
    result = slices_remaining
    return result

print(solution())