def solution():
    """A town council began the decade by planting cherry trees around the neighborhood to make the neighborhood look more welcoming. By the end of the decade, they have planted twice as many cherry trees as they originally planned and have now realized that falling cherry blossom leaves are causing a problem. Each tree drops 100 leaves each during the fall. If the town council originally intended to plant 7 cherry trees, how many leaves now fall from the trees?"""
    original_trees = 7
    final_trees = 2 * original_trees
    leaves_per_tree = 100
    total_leaves = final_trees * leaves_per_tree
    result = total_leaves
    return result

print(solution())