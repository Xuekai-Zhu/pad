def solution():
    # Define the number of stones and the ratio of trees to stones
    stones = 40
    tree_ratio = 3

    # Calculate the number of trees
    trees = tree_ratio * stones

    # Calculate the combined number of trees and stones
    total_trees_and_stones = trees + stones

    # Calculate the number of birds in the trees
    birds = 2 * total_trees_and_stones

    result = birds
    return result

print(solution())