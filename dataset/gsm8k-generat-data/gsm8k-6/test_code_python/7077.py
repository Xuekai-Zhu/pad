def solution():
    # Convert all measurements to feet
    initial_snow = 0.5  # feet of snow on the first day
    next_day_snow = 8 / 12  # feet of snow on the second day
    melted_snow = 2 / 12  # feet of snow melted over the next two days
    fifth_day_snow = 2 * initial_snow  # feet of snow received on the fifth day

    # Calculate the total amount of snow now
    total_snow = initial_snow + next_day_snow + fifth_day_snow - melted_snow
    result = total_snow
    return result

print(solution())