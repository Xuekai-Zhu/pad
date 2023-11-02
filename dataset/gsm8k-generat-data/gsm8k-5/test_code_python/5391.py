def solution():
    initial_marbles = 100  # Reggie's friend arrived with 100 marbles
    bet_per_game = 10  # They bet 10 marbles per game
    marbles_after_9_games = 90  # Reggie has 90 marbles after 9 games

    # Calculate the total number of marbles bet in 9 games
    total_bet = 9 * bet_per_game

    # Calculate the number of marbles Reggie had initially
    initial_reggie_marbles = initial_marbles - (total_bet // 2)

    # Calculate the number of games Reggie lost
    games_lost = (initial_reggie_marbles - marbles_after_9_games) // bet_per_game
    result = games_lost
    return result

print(solution())