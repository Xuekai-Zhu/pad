def solution():
    """Ragnar is a woodchopper. He can get 3 blocks of wood for every tree he cuts. If Ragnar chops 2 trees every day, how many blocks of woods does he get after 5 days?"""
    # Define the number of trees chopped per day
    TREES_PER_DAY = 2

    # Define the number of blocks of wood obtained per tree
    BLOCKS_PER_TREE = 3

    # Calculate the number of trees chopped in 5 days
    trees_chopped = TREES_PER_DAY * 5

    # Calculate the total number of blocks of wood obtained
    total_blocks = trees_chopped * BLOCKS_PER_TREE

    # Display the total number of blocks of wood
    result = total_blocks
    return result

print(solution())