def solution():
    """Jess and her family play Jenga, a game made up of 54 stacked blocks in which each player removes one block in turns until the stack falls. The 5 players, including Jess, play 5 rounds in which each player removes one block. In the sixth round, Jess's father goes first. He removes a block, causing the tower to almost fall. Next, Jess tries to remove another block knocking down the tower. How many blocks did the tower have before Jess's turn?"""
    total_blocks = 54
    blocks_removed = 5 * 5 + 1 # 5 rounds played by 5 players, plus one for the father's turn
    remaining_blocks = total_blocks - blocks_removed
    result = remaining_blocks
    return result

print(solution())