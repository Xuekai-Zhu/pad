def solution():
    """Felix is chopping down trees in his backyard. For every 13 trees he chops down he needs to get his axe resharpened. It cost him $5 to sharpen his axe. If he spends $35 on axe sharpening, at least how many trees has he chopped down?"""
    # Define the cost to sharpen the axe and the number of trees per sharpening
    SHARPENING_COST = 5
    TREES_PER_SHARPENING = 13

    # Calculate the number of times Felix had to sharpen his axe
    sharpening_count = 35 // SHARPENING_COST

    # Calculate the minimum number of trees he chopped down
    min_trees_chopped = sharpening_count * TREES_PER_SHARPENING

    result = min_trees_chopped
    return result

print(solution())