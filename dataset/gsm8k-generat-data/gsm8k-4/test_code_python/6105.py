def solution():
    """A town council began the decade by planting cherry trees around the neighborhood to make the neighborhood look more welcoming. By the end of the decade, they have planted twice as many cherry trees as they originally planned and have now realized that falling cherry blossom leaves are causing a problem. Each tree drops 100 leaves each during the fall. If the town council originally intended to plant 7 cherry trees, how many leaves now fall from the trees?"""
    # Define the original number of cherry trees planted
    original_trees = 7

    # Calculate the final number of cherry trees planted
    final_trees = original_trees * 2

    # Calculate the total number of leaves that fall in the fall season
    total_leaves = final_trees * 100

    # return the result
    result = total_leaves
    return result

print(solution())