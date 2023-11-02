def solution():
    """Amiyah is cutting some trees to build a cow shade. For every tree she cuts, she plants 5 new trees. If there were 400 trees on her farm and she cut 20% of them, calculate the total number of trees on the farm."""
    initial_trees = 400
    cut_trees = initial_trees * 0.2
    remaining_trees = initial_trees - cut_trees
    planted_trees = cut_trees * 5
    total_trees = remaining_trees + planted_trees
    result = total_trees
    return result

print(solution())