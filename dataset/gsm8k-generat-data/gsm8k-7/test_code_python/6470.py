def solution():
    workplace_to_market_distance = 30  # miles
    market_to_home_time = 0.5  # hours
    market_to_home_speed = 20  # miles per hour

    # Calculate the distance Greg travels from the farmer's market to his home
    market_to_home_distance = market_to_home_speed * market_to_home_time

    # Calculate the total distance Greg travels
    total_distance = workplace_to_market_distance + market_to_home_distance
    result = total_distance
    return result

print(solution())