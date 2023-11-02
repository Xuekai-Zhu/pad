def solution():
    """Sarah is playing tic-tac-toe. She wins $1 for every game she wins, $0 for every game she ties, and she loses $2 for every game she loses. If she played 100 games where she tied 40 of them, and she lost $30, how many games did she win?"""
    # Define the amount won and lost per game
    WIN_AMOUNT = 1
    TIE_AMOUNT = 0
    LOSS_AMOUNT = -2

    # Get the number of games played and the amount lost
    total_games = 100
    amount_lost = 30

    # Calculate the number of games won and tied
    games_tied = 40
    games_lost = amount_lost / LOSS_AMOUNT
    games_won = total_games - games_tied - games_lost

    # Display the number of games won
    result = games_won
    return result

print(solution())