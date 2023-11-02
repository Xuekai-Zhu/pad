def solution():
    """Marta is weighing fruit at the grocery store. The apples weigh four ounces each and the oranges
    weight 3 ounces. Each plastic bag in the grocery store can hold 49 ounces of fruit before it splits.
    If Martha wants to put an equal number of apples and oranges in each bag, and she wants to buy 3 full
    bags of fruit, how many ounces of apples should she buy?"""
    # Define the weight of each apple and orange
    APPLE_WEIGHT = 4
    ORANGE_WEIGHT = 3

    # Define the maximum weight of each bag
    MAX_WEIGHT = 49

    # Calculate the total weight of each bag if it has an equal number of apples and oranges
    bag_weight = (APPLE_WEIGHT + ORANGE_WEIGHT) * 2

    # Calculate the total weight of 3 bags
    total_weight = bag_weight * 3

    # Calculate the number of apples needed for 3 bags
    # (assuming equal number of apples and oranges in each bag)
    apples_needed = total_weight // APPLE_WEIGHT // 2

    # Calculate the weight of the needed apples
    apple_weight_needed = apples_needed * APPLE_WEIGHT

    # Return the result
    result = apple_weight_needed
    return result

print(solution())