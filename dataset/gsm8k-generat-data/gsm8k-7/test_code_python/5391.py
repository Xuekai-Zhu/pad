def solution():
    starting_marbles = 100
    bet_per_game = 10
    total_games = 9
    current_marbles = 90
    marbles_won = starting_marbles - current_marbles

    # Calculate the total number of bets made
    total_bets = total_games * bet_per_game

    # Calculate the total number of marbles lost by Reggie
    marbles_lost = total_bets - marbles_won

    # Calculate the number of games lost by Reggie
    games_lost = marbles_lost // bet_per_game
    result = games_lost
    return result

print(solution())