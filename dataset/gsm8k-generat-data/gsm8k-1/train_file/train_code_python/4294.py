def solution():
    """Jessica's family is 300 km away from New York. If they are traveling at the rate of 50 km/h and stop to rest for 30 minutes every 2 hours, how long will it take them to reach New York?"""
    total_distance = 300
    speed = 50
    rest_time = 0.5  # in hours
    rest_period = 2  # in hours
    travel_time = total_distance / speed
    number_of_rests = travel_time // rest_period
    total_rest_time = number_of_rests * rest_time
    total_time = travel_time + total_rest_time
    result = total_time
    return result

print(solution())