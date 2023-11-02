def solution():
    """Tom fills a 250 pound sandbag 80% full.  But the filling material he is using is 40% heavier than sand.  How much does the bag weigh?"""
    # Define the weight of the sandbag and the fill material's weight relative to sand
    sandbag_weight = 250
    fill_weight_ratio = 1.4

    # Calculate the weight of the fill material
    fill_weight = (sandbag_weight * 0.8) * fill_weight_ratio

    # Calculate the total weight of the sandbag with the fill material
    total_weight = sandbag_weight + fill_weight

    result = total_weight
    return result

print(solution())