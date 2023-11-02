def solution():
    """Jess and her family play Jenga, a game made up of 54 stacked blocks in which each player removes one block in turns until the stack falls. The 5 players, including Jess, play 5 rounds in which each player removes one block. In the sixth round, Jess's father goes first. He removes a block, causing the tower to almost fall. Next, Jess tries to remove another block knocking down the tower. How many blocks did the tower have before Jess's turn?"""
    # Define the number of blocks in a Jenga game
    BLOCKS_IN_GAME = 54

    # Calculate the number of blocks removed in the first 5 rounds (5 players each remove 1 block for 5 rounds)
    blocks_removed = 5 * 5

    # Calculate the remaining number of blocks before Jess's turn in the 6th round
    remaining_blocks = BLOCKS_IN_GAME - blocks_removed - 1  # subtract 1 for the block Jess's father removed

    # Display the number of blocks before Jess's turn
    result = remaining_blocks
    return result

print(solution())