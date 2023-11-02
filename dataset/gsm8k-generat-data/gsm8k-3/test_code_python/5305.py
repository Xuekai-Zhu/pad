def solution():
    """Natalie bought two cheesecakes, an apple pie, and a six-pack of muffins. The six-pack of muffins was two times more expensive than the cheesecake, and one cheesecake was only 25% cheaper than the apple pie. If the apple pie cost $12, how much did Natalie pay for all her shopping?"""
    # Define the cost of the apple pie
    APPLE_PIE_COST = 12

    # Calculate the cost of one cheesecake
    CHEESECAKE_COST = APPLE_PIE_COST * 1.25

    # Calculate the cost of the six-pack of muffins
    MUFFINS_COST = CHEESECAKE_COST * 2

    # Calculate the total cost of all the food
    total_cost = (2 * CHEESECAKE_COST) + APPLE_PIE_COST + MUFFINS_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())