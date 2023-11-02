def solution():
    total_games = 100  # Sarah played 100 games in total
    tie_games = 40  # Sarah tied 40 games
    lost_money = 30  # Sarah lost $30 in total

    # Calculate the total amount of money Sarah won from winning games
    money_from_wins = total_games - tie_games - lost_money / 2

    # Calculate the number of wins Sarah had
    num_of_wins = money_from_wins / 1
    result = num_of_wins
    return result

print(solution())