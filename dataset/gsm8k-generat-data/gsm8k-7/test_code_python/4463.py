def solution():
    player1_seeds = 78
    player2_seeds = 53
    player3_seeds = player2_seeds + 30

    # Calculate the total number of seeds eaten by all players
    total_seeds = player1_seeds + player2_seeds + player3_seeds
    result = total_seeds
    return result

print(solution())