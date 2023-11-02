def solution():
    distance = 300  # Jessica's family is 300 km away from New York
    speed = 50  # They are traveling at the rate of 50 km/h
    rest_time = 0.5  # They stop to rest for 30 minutes every 2 hours, which is 0.5 hours

    # Calculate the time it takes to travel without rest stops
    travel_time_no_rest_stops = distance / speed

    # Calculate the number of rest stops
    num_rest_stops = (travel_time_no_rest_stops // 2)

    # Calculate the total rest time
    total_rest_time = num_rest_stops * rest_time

    # Calculate the total travel time
    total_travel_time = travel_time_no_rest_stops + total_rest_time
    result = total_travel_time
    return result

print(solution())