def solution():
    """Jess and her family play Jenga, a game made up of 54 stacked blocks in which each player removes one block in turns until the stack falls. The 5 players, including Jess, play 5 rounds in which each player removes one block. In the sixth round, Jess's father goes first. He removes a block, causing the tower to almost fall. Next, Jess tries to remove another block knocking down the tower. How many blocks did the tower have before Jess's turn?"""
    # Define the initial number of blocks in the Jenga tower
    initial_blocks = 54

    # Calculate the total number of blocks removed in the first 5 rounds
    blocks_removed_rounds = 5 * 5

    # Calculate the total number of blocks remaining after the first 5 rounds
    blocks_remaining_rounds = initial_blocks - blocks_removed_rounds

    # Calculate the number of blocks removed in the sixth round
    blocks_removed_sixth = 1

    # Calculate the number of blocks remaining before Jess's turn
    blocks_remaining_jess_turn = blocks_remaining_rounds - blocks_removed_sixth

    result = blocks_remaining_jess_turn
    return result

print(solution())