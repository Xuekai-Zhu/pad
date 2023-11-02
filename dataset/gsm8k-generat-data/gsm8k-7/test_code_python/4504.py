def solution():
    miles_per_hour = 8
    driving_time = 5
    cool_down_time = 1
    total_time = 13

    # Calculate the total driving time
    num_driving_periods = total_time // (driving_time + cool_down_time)
    total_driving_time = num_driving_periods * driving_time

    # Calculate the total distance driven during driving time
    total_distance_driven = total_driving_time * miles_per_hour

    result = total_distance_driven
    return result

print(solution())