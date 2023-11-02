def solution():
    distance = 143  # miles
    speed_with_load = 11  # miles per hour
    speed_without_load = 13  # miles per hour
    rest_stop_time = 0.5  # hours

    # Calculate the time it takes for Mobius to travel from Florence to Rome
    time_to_rome = distance / speed_with_load
    time_to_rome += rest_stop_time * 2  # add 2 rest stops

    # Calculate the time it takes for Mobius to travel from Rome to Florence
    time_to_florence = distance / speed_without_load
    time_to_florence += rest_stop_time * 2  # add 2 rest stops

    # Calculate the total time for the whole trip
    total_time = time_to_rome + time_to_florence
    result = total_time
    return result

print(solution())