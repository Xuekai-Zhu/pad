def solution():
    # Calculate the total marbles bet in 9 games
    total_bet = 9 * 10

    # Calculate the total marbles that Reggie won
    total_won = 100 - 90

    # Calculate the total marbles that Reggie bet
    total_reggie_bet = total_bet - total_won

    # Calculate the number of games Reggie lost
    games_lost = total_reggie_bet / 10
    result = games_lost
    return result

print(solution())