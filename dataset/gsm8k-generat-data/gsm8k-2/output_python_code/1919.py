def solution():
    """Blanch has 15 slices of pizza in the fridge. During breakfast, she eats 4 slices. At lunch, Blanch eats 2 slices, then takes two slices as a snack. Finally, she consumes 5 slices for dinner. How many slices of pizza are left?"""
    initial_slices = 15
    breakfast_slices = 4
    lunch_slices = 2
    snack_slices = 2
    dinner_slices = 5
    total_slices_eaten = breakfast_slices + lunch_slices + snack_slices + dinner_slices
    remaining_slices = initial_slices - total_slices_eaten
    result = remaining_slices
    return result

print(solution())