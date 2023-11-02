def solution():
    """Amiyah is cutting some trees to build a cow shade. For every tree she cuts, she plants 5 new trees. If there were 400 trees on her farm and she cut 20% of them, calculate the total number of trees on the farm."""
    total_trees = 400
    cut_percentage = 0.2
    cut_trees = total_trees * cut_percentage
    trees_planted = cut_trees * 5
    remaining_trees = total_trees - cut_trees + trees_planted
    result = remaining_trees
    return result

print(solution())