def solution():
    blocks_per_tree = 3  # Ragnar can get 3 blocks of wood for every tree he cuts
    trees_per_day = 2  # Ragnar chops 2 trees every day
    days = 5  # Ragnar wants to know how many blocks of wood he will get after 5 days

    # Calculate the total number of blocks of wood Ragnar will get after 5 days
    total_blocks = blocks_per_tree * trees_per_day * days

    result = total_blocks
    return result

print(solution())