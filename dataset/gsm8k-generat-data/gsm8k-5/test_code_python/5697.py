def solution():
    total_slices = 12  # Neeley sliced the bread into 12 pieces
    breakfast_slices = total_slices / 3  # Neeley's family ate a third of the bread slices
    lunch_slices = 2  # Neeley used 2 slices to make a sandwich for lunch

    # Calculate the remaining slices of bread
    remaining_slices = total_slices - breakfast_slices - lunch_slices
    result = remaining_slices
    return result

print(solution())