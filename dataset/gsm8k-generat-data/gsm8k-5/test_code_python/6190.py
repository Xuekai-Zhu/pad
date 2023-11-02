def solution():
    hours_slept_dec = 6.5  # Angela slept 6.5 hours every night in December
    hours_slept_jan = 8.5  # Angela began sleeping 8.5 hours a night in January

    # Calculate the total hours of sleep in December and January
    total_hours_dec = hours_slept_dec * 31  # There are 31 days in December
    total_hours_jan = hours_slept_jan * 31  # There are 31 days in January

    # Calculate the difference in total hours of sleep between December and January
    extra_hours = total_hours_jan - total_hours_dec
    result = extra_hours
    return result

print(solution())