def solution():
    # Calculate the distance Greg drives to the farmers market
    distance_to_market = 30

    # Calculate the distance Greg travels on his way home
    time_taken = 0.5  # 30 minutes = 0.5 hours
    speed = 20  # miles per hour
    distance_on_way_home = time_taken * speed

    # Calculate the total distance Greg travels
    total_distance = distance_to_market + distance_on_way_home
    result = total_distance
    return result

print(solution())