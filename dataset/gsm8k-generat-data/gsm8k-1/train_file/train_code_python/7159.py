def solution():
    """Jennie drives to her son’s house in 5 hours when there is heavy traffic. When there is no traffic the same trip takes only 4 hours. If her son's house is 200 miles away, what is the difference between her average speed when there is heavy traffic and when there is no traffic?"""
    distance = 200
    heavy_traffic_time = 5
    no_traffic_time = 4
    heavy_traffic_speed = distance / heavy_traffic_time
    no_traffic_speed = distance / no_traffic_time
    speed_difference = heavy_traffic_speed - no_traffic_speed
    result = speed_difference
    
    return result

print(solution())