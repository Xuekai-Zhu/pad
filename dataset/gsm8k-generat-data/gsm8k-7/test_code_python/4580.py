def solution():
    total_games = 100
    tied_games = 40
    lost_money = 30
    win_money = 1

    # Calculate the total money received from tied games
    tied_money = tied_games * 0

    # Calculate the total money lost from lost games
    lost_money = lost_money

    # Calculate the total money received from won games
    won_money = total_games * win_money - (tied_money + lost_money)

    # Calculate the number of won games
    num_won_games = won_money / win_money

    result = num_won_games
    return result

print(solution())