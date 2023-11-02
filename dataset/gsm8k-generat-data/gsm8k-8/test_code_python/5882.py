def solution():
    # Calculate the number of slices needed for one weekend
    weekend_slices = 2 * (1 + 0.5*2)  # 1 slice each for Suzanne and her husband, and 0.5 slice each for her daughters

    # Calculate the number of loaves needed for one weekend
    weekend_loaves = weekend_slices/12

    # Calculate the number of loaves needed for one year
    year_loaves = weekend_loaves * 52

    result = year_loaves
    return result

print(solution())