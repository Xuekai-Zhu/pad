def solution():
    """Irene shares half of a small apple with her dog every day.  A small apple weighs about 1/4 of a pound.  She can currently buy apples for $2.00 a pound.  How much will she spend so that she and her dog have enough apples to last for 2 weeks?"""
    # Define the weight of a small apple and the number of days to last
    APPLE_WEIGHT = 0.25
    DAYS = 14

    # Calculate the total amount of apples needed
    total_apples = (0.5 * DAYS) / APPLE_WEIGHT

    # Calculate the total cost of the apples
    cost = total_apples * 2.00

    # Display the total cost
    result = cost
    return result

print(solution())