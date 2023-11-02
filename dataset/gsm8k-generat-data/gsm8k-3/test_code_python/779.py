def solution():
    """The flowers cost $9, the clay pot costs $20 more than the flower, and the bag of soil costs $2 less than the flower.  How much does it cost to plant the flowers?"""
    # Define the cost of the flowers, clay pot, and bag of soil
    FLOWER_COST = 9
    CLAY_POT_COST = FLOWER_COST + 20
    SOIL_COST = FLOWER_COST - 2

    # Calculate the total cost to plant the flowers
    total_cost = FLOWER_COST + CLAY_POT_COST + SOIL_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())