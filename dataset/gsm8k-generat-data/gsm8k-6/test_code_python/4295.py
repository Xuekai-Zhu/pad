def solution():
    # Calculate the total travel time including rest stops
    travel_time = 300 / 50  # time without rest stops
    rest_stops = travel_time // 2  # number of rest stops
    rest_time = rest_stops * 0.5  # time spent resting
    total_time = travel_time + rest_time  # total travel time including rest stops
    result = total_time
    return result

print(solution())