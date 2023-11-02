def solution():
    # Convert jog time to hours
    jog_time = 0.5

    # Calculate total jogging time in first week
    first_week_jog_time = jog_time * 3

    # Calculate total jogging time in second week
    second_week_jog_time = jog_time * 5

    # Calculate total jogging time for two weeks
    total_jog_time = first_week_jog_time + second_week_jog_time

    # Convert total jogging time to hours
    total_jog_time_hours = total_jog_time / 2

    result = total_jog_time_hours
    return result

print(solution())