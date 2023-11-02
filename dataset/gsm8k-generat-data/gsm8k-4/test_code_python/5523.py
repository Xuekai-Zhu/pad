def solution():
    """Joe likes to play video games and he normally spends $50 a month on video games. Joe also sells his games for $30 each once he is done playing them. If he starts with $240, how many months can he buy games at $50 and sell them at $30 before he is out of money?"""
    # Define the initial amount of money Joe has
    initial_money = 240

    # Define the cost and profit of each game
    game_cost = 50
    game_profit = 30

    # Initialize the number of months Joe can play games
    months = 0

    # Calculate the number of months Joe can play games before running out of money
    while initial_money >= game_cost:
        # Subtract the cost of buying a game
        initial_money -= game_cost
        
        # Add the profit from selling a game
        initial_money += game_profit
        
        # Increment the month counter
        months += 1
        
    # Return the result
    result = months
    return result

print(solution())