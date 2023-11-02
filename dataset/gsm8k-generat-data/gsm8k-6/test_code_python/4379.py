def solution():
    # Calculate the driving time with rest stops
    driving_time = 600 / 50  # total distance/average speed
    num_rest_stops = driving_time // 2  # number of rest stops taken
    rest_stop_time = num_rest_stops * 15  # total rest stop time in minutes
    refill_time = 10  # time taken to refill gas

    # Calculate the total travel time
    total_time = driving_time + rest_stop_time + (refill_time / 60)  # refill time converted to hours
    result = total_time * 60  # converted to minutes
    return result

print(solution())