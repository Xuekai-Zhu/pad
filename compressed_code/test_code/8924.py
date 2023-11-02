def solution():
    
    players = 5
    rounds = 5
    blocks_per_round = players
    initial_blocks = 54
    blocks_left = initial_blocks - (rounds * blocks_per_round)
    blocks_left -= 1 
    result = blocks_left
    return result

print(solution())