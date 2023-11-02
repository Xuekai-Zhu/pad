def solution():
    # Determine the number of slices needed for each weekend day
    total_slices_per_day = 2 + 0.5*2

    # Determine the number of loaves needed per weekend day
    loaves_per_day = total_slices_per_day / 12

    # Multiply by the number of weekend days in a year to get the total number of loaves needed
    loaves_per_year = loaves_per_day * 104

    result = loaves_per_year
    return result

print(solution())