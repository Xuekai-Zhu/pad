def solution():
    total_slices = 24  # The loaf of bread has 24 slices
    abby_slices_per_day = 2  # Abby can eat 2 slices per day
    josh_slices_per_day = 2 * abby_slices_per_day  # Josh can eat twice as much as Abby

    # Calculate the number of days the loaf will last
    num_days = total_slices / (abby_slices_per_day + josh_slices_per_day)
    result = num_days
    return result

print(solution())