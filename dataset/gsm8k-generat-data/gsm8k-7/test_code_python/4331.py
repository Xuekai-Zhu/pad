def solution():
    seconds_per_minute = 60
    minutes_per_hour = 60
    seconds_per_hour = seconds_per_minute * minutes_per_hour

    # Calculate the number of instances of data recorded per hour
    data_instances_per_hour = seconds_per_hour // 5

    result = data_instances_per_hour
    return result

print(solution())