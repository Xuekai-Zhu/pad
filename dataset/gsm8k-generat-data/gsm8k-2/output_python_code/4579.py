def solution():
    """Sarah is playing tic-tac-toe. She wins $1 for every game she wins, $0 for every game she ties, and she loses $2 for every game she loses. If she played 100 games where she tied 40 of them, and she lost $30, how many games did she win?"""
    total_games = 100
    ties = 40
    lost_money = 30

    # Money earned from wins
    earned_money = total_games - ties - lost_money/2

    # Number of wins
    wins = earned_money/1

    result = wins
    return result

print(solution())