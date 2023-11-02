def solution():
    """Marta is weighing fruit at the grocery store. The apples weigh four ounces each and the oranges weight 3 ounces. Each plastic bag in the grocery store can hold 49 ounces of fruit before it splits. If Martha wants to put an equal number of apples and oranges in each bag, and she wants to buy 3 full bags of fruit, how many ounces of apples should she buy?"""
    # Define the weight of each apple and orange
    APPLE_WEIGHT = 4
    ORANGE_WEIGHT = 3

    # Define the maximum weight a bag can hold
    MAX_WEIGHT = 49

    # Calculate the maximum number of apples and oranges that can fit in a bag
    max_apples = MAX_WEIGHT // (APPLE_WEIGHT + ORANGE_WEIGHT)
    max_oranges = max_apples

    # Calculate the total weight of each type of fruit in a bag
    total_apple_weight = max_apples * APPLE_WEIGHT
    total_orange_weight = max_oranges * ORANGE_WEIGHT

    # Calculate the total weight of fruit in 3 bags
    total_weight = 3 * MAX_WEIGHT

    # Calculate the number of apples needed to fill 3 bags
    num_apples = (total_weight - total_orange_weight) // APPLE_WEIGHT

    # Display the number of ounces of apples needed
    result = num_apples * APPLE_WEIGHT
    return result

print(solution())