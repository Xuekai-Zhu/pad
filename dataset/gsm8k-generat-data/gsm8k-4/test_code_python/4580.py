def solution():
    """Sarah is playing tic-tac-toe. She wins $1 for every game she wins, $0 for every game she ties, and she loses $2 for every game she loses. If she played 100 games where she tied 40 of them, and she lost $30, how many games did she win?"""
    # Define the number of tied games and the amount lost
    tied_games = 40
    amount_lost = 30

    # Calculate the total amount won from tied games
    tied_winnings = 0

    # Calculate the total amount won from winning games
    winnings = 0

    # Calculate the total number of games played
    total_games = 100

    # Calculate the total amount spent on losing games
    lost_amount = amount_lost + (total_games - tied_games) * 2

    # Calculate the total amount won
    total_won = tied_winnings + winnings - lost_amount

    # Calculate the number of games won
    games_won = total_won

    # Return the result
    result = games_won
    return result

print(solution())