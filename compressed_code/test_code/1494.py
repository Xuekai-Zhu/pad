def solution():
    
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