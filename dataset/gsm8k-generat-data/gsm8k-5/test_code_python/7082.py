def solution():
    total_slices = 12  # Donna cut her pizza into 12 slices
    lunch_slices = total_slices / 2  # Donna ate half the pizza for lunch
    remaining_slices = total_slices - lunch_slices  # Calculate the number of remaining slices
    dinner_slices = remaining_slices / 3  # Donna ate 1/3 of the remaining slices for dinner
    remaining_slices -= dinner_slices  # Subtract the dinner slices from the remaining slices

    result = remaining_slices  # The remaining slices are the slices left for Donna's lunch tomorrow
    return result

print(solution())