def solution():
    distance = 200  # Jennie's son's house is 200 miles away

    # Calculate Jennie's speed when there is heavy traffic
    speed_heavy_traffic = distance / 5

    # Calculate Jennie's speed when there is no traffic
    speed_no_traffic = distance / 4

    # Calculate the difference in average speed between the two scenarios
    avg_speed_diff = speed_no_traffic - speed_heavy_traffic
    result = avg_speed_diff
    return result

print(solution())