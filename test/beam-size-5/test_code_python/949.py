def solution():
    sleep_speed = 10  # in p.m.
    sleep_time = 6  # in minutes
    cameras_sleepwalking_time = (2 * 15) + 38  # in minutes
    sleep_time_difference = 5  # in minutes

    # Calculate the total sleep time
    total_sleep_time = sleep_speed * cameras_sleepwalking_time + sleep_time_difference

    # Calculate the total sleep time on the bed
    total_sleep_time = sleep_time + sleep_time_difference
    result = total_sleep_time
    return result

print(solution())