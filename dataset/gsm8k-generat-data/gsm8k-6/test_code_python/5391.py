def solution():
    # Calculate how many marbles Reggie had at the start
    starting_marbles = 90 + 10*9  # Reggie won 9 games, so he won 90 marbles in those games and started with 10 marbles

    # Calculate how many games Reggie lost
    games_lost = (starting_marbles - 100) // 10  # Reggie needs to have 100 marbles, so he lost (starting_marbles - 100) marbles and each game had a bet of 10 marbles
    result = games_lost
    return result

print(solution())