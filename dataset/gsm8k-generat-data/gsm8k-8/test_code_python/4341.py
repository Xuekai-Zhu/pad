def solution():
    # Calculate the duration of rain on the first day
    first_day_duration = 10

    # Calculate the duration of rain on the second day
    second_day_duration = first_day_duration + 2

    # Calculate the duration of rain on the third day
    third_day_duration = 2 * second_day_duration

    # Calculate the total duration of rain over the three days
    total_duration = first_day_duration + second_day_duration + third_day_duration
    result = total_duration
    return result

print(solution())