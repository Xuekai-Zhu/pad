def solution():
    
    # Define the weight of each portion of flour
    PORTION_WEIGHT = 2

    # Define the number of portions in each bag
    PORTIONS_PER_BAG = 8

    # Calculate the total weight of flour in each bag
    total_weight = PORTION_WEIGHT * PORTIONS_PER_BAG

    # Calculate the total weight of flour in three bags
    total_weight_3_bags = total_weight * 3

    # Display the total weight of flour in three bags
    result = total_weight_3_bags
    return result

print(solution())