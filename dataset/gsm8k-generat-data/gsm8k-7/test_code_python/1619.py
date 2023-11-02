def solution():
    blocks_per_tree = 3
    trees_per_day = 2
    num_days = 5

    # Calculate the total number of trees Ragnar chops
    total_trees = trees_per_day * num_days

    # Calculate the total number of blocks of wood Ragnar gets
    total_blocks = total_trees * blocks_per_tree
    result = total_blocks
    return result

print(solution())