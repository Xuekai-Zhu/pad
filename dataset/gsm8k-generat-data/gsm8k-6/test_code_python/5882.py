def solution():
    # Calculate the total number of slices needed for one weekend
    weekend_slices = 2 + 0.5*2  # Suzanne and her husband each have 1 whole slice, and her daughters split 1 slice

    # Calculate the number of loaves needed for one weekend
    loaves_needed = weekend_slices / 12  # using a thick sliced bread that comes 12 slices per loaf

    # Calculate the number of loaves needed for 52 weeks
    loaves_per_year = loaves_needed * 104  # 2 days per week for 52 weeks

    result = loaves_per_year
    return result

print(solution())