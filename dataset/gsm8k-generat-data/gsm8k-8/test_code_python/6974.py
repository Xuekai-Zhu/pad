def solution():
    # Calculate the total slices of bread consumed per day
    slices_per_day = 4 * (3 + 2)

    # Calculate the total slices of bread consumed in 5 days
    slices_in_five_days = slices_per_day * 5

    # Calculate the total number of slices in 5 loaves of bread
    total_slices_in_five_loaves = 12 * 5

    # Calculate the number of days the 5 loaves of bread will last
    days_of_bread = total_slices_in_five_loaves // slices_in_five_days
    result = days_of_bread
    return result

print(solution())