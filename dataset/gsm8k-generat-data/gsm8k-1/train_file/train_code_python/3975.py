def solution():
    """Jess and her family play Jenga, a game made up of 54 stacked blocks in which each player removes one block in turns until the stack falls. The 5 players, including Jess, play 5 rounds in which each player removes one block. In the sixth round, Jess's father goes first. He removes a block, causing the tower to almost fall. Next, Jess tries to remove another block knocking down the tower. How many blocks did the tower have before Jess's turn?"""
    players = 5
    rounds = 5
    blocks_per_round = players
    initial_blocks = 54
    blocks_left = initial_blocks - (rounds * blocks_per_round)
    blocks_left -= 1 # one block removed by Jess's father
    result = blocks_left
    return result

print(solution())