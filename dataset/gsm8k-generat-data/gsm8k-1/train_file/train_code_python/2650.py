def solution():
    """Felix is chopping down trees in his backyard. For every 13 trees he chops down he needs to get his axe resharpened. It cost him $5 to sharpen his axe. If he spends $35 on axe sharpening, at least how many trees has he chopped down?"""
    trees_per_sharpening = 13
    cost_per_sharpening = 5
    total_cost = 35
    num_sharpenings = total_cost / cost_per_sharpening
    min_trees_chopped = trees_per_sharpening * num_sharpenings
    result = min_trees_chopped
    return result

print(solution())