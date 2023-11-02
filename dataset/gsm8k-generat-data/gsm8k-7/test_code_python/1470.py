def solution():
    jog_time = 30  # minutes
    tues_extra = 5  # minutes
    fri_extra = 25  # minutes

    # Calculate total jog time for the weekdays
    total_weekday_jog_time = (jog_time * 3) + (jog_time + tues_extra) + (jog_time + fri_extra)

    # Convert the total jog time to hours
    total_jog_hours = total_weekday_jog_time / 60

    result = total_jog_hours
    return result

print(solution())