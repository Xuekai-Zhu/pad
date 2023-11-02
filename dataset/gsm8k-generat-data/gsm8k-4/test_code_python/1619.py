def solution():
    """Ragnar is a woodchopper. He can get 3 blocks of wood for every tree he cuts. If Ragnar chops 2 trees every day, how many blocks of woods does he get after 5 days?"""
    # Define the number of trees Ragnar cuts per day
    trees_per_day = 2

    # Calculate the total number of trees cut after 5 days
    total_trees = trees_per_day * 5

    # Calculate the total number of blocks of wood obtained
    total_blocks = total_trees * 3

    # return the result
    result = total_blocks
    return result

print(solution())