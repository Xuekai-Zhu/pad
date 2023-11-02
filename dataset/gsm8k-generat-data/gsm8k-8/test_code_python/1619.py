def solution():
    # Define the number of trees and blocks of wood
    trees_per_day = 2
    blocks_per_tree = 3

    # Calculate the total number of trees cut down
    total_trees_cut = trees_per_day * 5

    # Calculate the total number of blocks of wood
    total_blocks = total_trees_cut * blocks_per_tree
    result = total_blocks
    return result

print(solution())