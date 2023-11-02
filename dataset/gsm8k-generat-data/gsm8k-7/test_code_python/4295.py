def solution():
    distance = 300
    speed = 50
    rest_time = 0.5  # 30 minutes in hours
    rest_interval = 2  # in hours

    # Calculate the time it takes to travel without rest stops
    travel_time = distance / speed

    # Calculate the number of rest stops they will have to take
    num_rests = travel_time // rest_interval

    # Calculate the total time spent on rest stops
    total_rest_time = num_rests * rest_time

    # Add the total time spent resting to the travel time
    total_time = travel_time + total_rest_time
    result = total_time
    return result

print(solution())