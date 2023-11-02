def solution():
    num_slices = 12

    # Calculate the number of slices Donna ate for lunch
    slices_for_lunch = num_slices / 2

    # Calculate the number of slices remaining after lunch
    remaining_slices = num_slices - slices_for_lunch

    # Calculate the number of slices Donna ate for dinner
    slices_for_dinner = remaining_slices / 3

    # Calculate the number of slices remaining for tomorrow's lunch
    slices_for_tomorrow = remaining_slices - slices_for_dinner
    result = slices_for_tomorrow
    return result

print(solution())