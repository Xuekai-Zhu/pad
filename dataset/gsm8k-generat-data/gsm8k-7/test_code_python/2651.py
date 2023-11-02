def solution():
    trees_per_sharpening = 13
    cost_per_sharpening = 5
    total_sharpening_cost = 35

    # Calculate the number of times Felix had to get his axe resharpened
    num_sharpenings = total_sharpening_cost / cost_per_sharpening

    # Calculate the minimum number of trees Felix chopped down
    min_trees_chopped = (num_sharpenings * trees_per_sharpening) + 1   # add one to account for any trees chopped after the last sharpening

    result = min_trees_chopped
    return result

print(solution())