def solution():
    """Sarah is playing tic-tac-toe. She wins $1 for every game she wins, $0 for every game she ties, and she loses $2 for every game she loses. If she played 100 games where she tied 40 of them, and she lost $30, how many games did she win?"""
    total_games = 100
    tied_games = 40
    lost_money = 30
    total_money = -1*tied_games*0 + 1*(total_games-tied_games-lost_money) + (-2*lost_money)
    num_wins = (total_money + 2*tied_games) / 3
    result = num_wins
    
    return result

print(solution())