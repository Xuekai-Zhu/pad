def solution():
    """Jennie drives to her son’s house in 5 hours when there is heavy traffic. When there is no traffic the same trip takes only 4 hours. If her son's house is 200 miles away, what is the difference between her average speed when there is heavy traffic and when there is no traffic?"""
    # Distance between Jennie's house and her son's house
    distance = 200

    # Time taken to drive to her son's house with heavy traffic
    time_heavy_traffic = 5

    # Time taken to drive to her son's house with no traffic
    time_no_traffic = 4

    # Speed with heavy traffic
    speed_heavy_traffic = distance / time_heavy_traffic

    # Speed with no traffic
    speed_no_traffic = distance / time_no_traffic

    # Difference between the two speeds
    difference = speed_heavy_traffic - speed_no_traffic

    # Display the difference in speeds
    result = difference
    return result

print(solution())