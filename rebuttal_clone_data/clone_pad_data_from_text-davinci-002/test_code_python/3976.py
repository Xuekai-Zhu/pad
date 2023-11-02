def solution ():
    blocks = 54
    players = 5
    rounds = 5
    blocks_per_round = 1
    blocks_removed = players * rounds * blocks_per_round
    blocks_left = blocks - blocks_removed
    result = blocks_left
    
    return result

print(solution())