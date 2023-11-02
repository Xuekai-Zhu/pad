def solution():
    """Tom fills a 250 pound sandbag 80% full.  But the filling material he is using is 40% heavier than sand.  How much does the bag weigh?"""
    # Define the weight of the sandbag and the fill material density ratio
    SANDBAG_WEIGHT = 250
    FILL_MATERIAL_RATIO = 1.4

    # Calculate the weight of the fill material
    fill_weight = SANDBAG_WEIGHT * 0.8 * FILL_MATERIAL_RATIO

    # Calculate the total weight of the sandbag and fill material
    total_weight = SANDBAG_WEIGHT + fill_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())