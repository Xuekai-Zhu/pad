def solution():
    """Jessica's family is 300 km away from New York. If they are traveling at the rate of 50 km/h and stop to rest for 30 minutes every 2 hours, how long will it take them to reach New York?"""
    distance = 300
    speed = 50
    rest_time = 0.5
    time_to_reach = distance / speed
    rest_periods = time_to_reach // 2
    total_rest_time = rest_periods * rest_time
    total_time = time_to_reach + total_rest_time
    result = total_time
    return result

print(solution())