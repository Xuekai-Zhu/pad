def solution():
    """Felix is chopping down trees in his backyard. For every 13 trees he chops down he needs to get his axe resharpened. It cost him $5 to sharpen his axe. If he spends $35 on axe sharpening, at least how many trees has he chopped down?"""
    # Define the number of trees chopped down between each axe sharpening
    TREES_PER_SHARPENING = 13

    # Define the cost to sharpen the axe
    SHARPENING_COST = 5

    # Calculate the number of times Felix had to sharpen his axe
    sharpen_count = 35 // SHARPENING_COST

    # Calculate the minimum number of trees chopped down
    min_trees_chopped = (sharpen_count - 1) * TREES_PER_SHARPENING

    # Display the minimum number of trees chopped down
    result = min_trees_chopped
    return result

print(solution())