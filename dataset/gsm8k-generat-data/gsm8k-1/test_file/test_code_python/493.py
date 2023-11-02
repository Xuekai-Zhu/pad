def solution():
    """
    Paul is driving a car twice a day: in the morning, and in the afternoon. He did that for 14 days. Each morning ride cost
    him about $6, and each afternoon ride, about $2. How much money did he spend on driving his car during these two weeks?
    """
    morning_cost = 6
    afternoon_cost = 2
    num_rides = 2 * 14
    total_cost = (morning_cost + afternoon_cost) * num_rides
    result = total_cost
    return result

print(solution())