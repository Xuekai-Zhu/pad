def solution():
    # Calculate the time taken for Mobius to travel from Florence to Rome with a typical load and two rest stops
    distance = 143  # miles
    speed_with_load = 11  # miles per hour
    time_travel_with_load = distance / speed_with_load  # hours
    time_rest_stop = 0.5  # hours
    total_time_with_load = time_travel_with_load + 2 * time_rest_stop  # hours

    # Calculate the time taken for Mobius to travel from Rome to Florence without a load and two rest stops
    speed_without_load = 13  # miles per hour
    time_travel_without_load = distance / speed_without_load  # hours
    total_time_without_load = time_travel_without_load + 2 * time_rest_stop  # hours

    # Calculate the total time taken for the round trip
    total_time = total_time_with_load + total_time_without_load

    result = total_time
    return result

print(solution())