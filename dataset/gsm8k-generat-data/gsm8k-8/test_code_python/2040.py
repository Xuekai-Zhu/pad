def solution():
    # Calculate the total number of slices
    total_slices = 8 + 14
  
    # Subtract the number of slices already eaten
    remaining_slices = total_slices - 2 * 9

    # Divide the remaining slices by the number of people
    slices_per_person = remaining_slices / 2

    result = slices_per_person
    return result

print(solution())