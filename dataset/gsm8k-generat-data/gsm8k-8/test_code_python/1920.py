def solution():
    # Define the initial number of pizza slices
    initial_slices = 15

    # Calculate the total number of slices Blanch eats
    total_eaten = 4 + 2 + 2 + 5

    # Calculate the remaining number of pizza slices
    remaining_slices = initial_slices - total_eaten
    result = remaining_slices
    return result

print(solution())