def solution():
    snow_on_first_day = 0.5
    snow_on_second_day = 8/12  # converting 8 inches to feet
    melted_snow = 2/12  # converting 2 inches to feet
    snow_on_fifth_day = 2 * snow_on_first_day

    total_snow = snow_on_first_day + snow_on_second_day - melted_snow + snow_on_fifth_day
    result = total_snow
    return result

print(solution())