def solution():
    """Jennie drives to her son’s house in 5 hours when there is heavy traffic. When there is no traffic the same trip takes only 4 hours. If her son's house is 200 miles away, what is the difference between her average speed when there is heavy traffic and when there is no traffic?"""
    # Define the distance to Jennie's son's house
    distance = 200

    # Calculate Jennie's average speed when there is heavy traffic
    heavy_traffic_speed = distance / 5

    # Calculate Jennie's average speed when there is no traffic
    no_traffic_speed = distance / 4

    # Calculate the difference in average speed
    speed_difference = heavy_traffic_speed - no_traffic_speed

    # Return the speed difference
    result = speed_difference
    return result

print(solution())