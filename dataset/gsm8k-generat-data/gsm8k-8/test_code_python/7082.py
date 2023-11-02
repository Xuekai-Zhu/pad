def solution():
    # Calculate the number of slices Donna had for lunch
    slices_for_lunch = 12 / 2

    # Calculate the number of slices remaining after lunch
    slices_after_lunch = 12 - slices_for_lunch

    # Calculate the number of slices Donna had for dinner
    slices_for_dinner = slices_after_lunch / 3

    # Calculate the number of slices remaining for tomorrow's lunch
    slices_for_tomorrow = slices_after_lunch - slices_for_dinner

    result = slices_for_tomorrow
    return result

print(solution())