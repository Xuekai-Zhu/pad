def solution():
    initial_slices = 15  # Blanch starts with 15 slices of pizza
    breakfast_slices = 4  # Blanch eats 4 slices for breakfast
    lunch_slices = 2  # Blanch eats 2 slices for lunch
    snack_slices = 2  # Blanch eats 2 slices for a snack
    dinner_slices = 5  # Blanch eats 5 slices for dinner

    # Calculate the total number of slices Blanch eats
    eaten_slices = breakfast_slices + lunch_slices + snack_slices + dinner_slices

    # Calculate the number of slices left
    remaining_slices = initial_slices - eaten_slices
    result = remaining_slices
    return result

print(solution())