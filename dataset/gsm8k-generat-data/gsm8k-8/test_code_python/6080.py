def solution():
    # Define the number of slices eaten by each person
    bob_slices = 6
    tom_slices = 4
    sally_slices = 2
    jerry_slices = 3

    # Calculate the total number of slices eaten
    total_slices_eaten = bob_slices + tom_slices + sally_slices + jerry_slices

    # Calculate the total number of slices in 2 pizzas
    total_slices = 24

    # Calculate the number of slices left over
    slices_left = total_slices - total_slices_eaten
    result = slices_left
    return result

print(solution())