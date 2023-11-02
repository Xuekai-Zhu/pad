def solution():
    # Calculate the number of blocks of wood Ragnar gets in 5 days
    blocks_per_tree = 3  # blocks of wood per tree
    trees_per_day = 2  # number of trees Ragnar cuts every day
    days = 5  # number of days
    total_blocks = blocks_per_tree * trees_per_day * days  # total blocks of wood
    result = total_blocks
    return result

print(solution())