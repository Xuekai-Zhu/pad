def solution():
    """Felix is chopping down trees in his backyard. For every 13 trees he chops down he needs to get his axe resharpened. It cost him $5 to sharpen his axe. If he spends $35 on axe sharpening, at least how many trees has he chopped down?"""
    axe_sharpening_cost = 5
    total_axe_sharpenings = 35 / axe_sharpening_cost
    trees_per_sharpening = 13
    total_trees_chopped = (total_axe_sharpenings + 1) * trees_per_sharpening
    result = total_trees_chopped
    return result

print(solution())