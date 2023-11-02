def solution():
    """Irene shares half of a small apple with her dog every day. A small apple weighs about 1/4 of a pound. She can currently buy apples for $2.00 a pound. How much will she spend so that she and her dog have enough apples to last for 2 weeks?"""
    # Define the weight of a small apple and the number of days in 2 weeks
    APPLE_WEIGHT = 1/4
    DAYS = 14

    # Calculate the total apples needed for 2 weeks
    total_apples = (1/2) * DAYS

    # Calculate the total weight of apples needed for 2 weeks
    total_weight = total_apples * APPLE_WEIGHT

    # Calculate the total cost for 2 weeks
    cost = total_weight * 2

    result = cost
    return result

print(solution())