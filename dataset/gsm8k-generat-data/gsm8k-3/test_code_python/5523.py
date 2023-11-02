def solution():
    """Joe likes to play video games and he normally spends $50 a month on video games.  Joe also sells his games for $30 each once he is done playing them. If he starts with $240, how many months can he buy games at $50 and sell them at $30 before he is out of money?"""
    # Define the monthly cost of games and the selling price of games
    monthly_cost = 50
    selling_price = 30

    # Define the starting amount of money
    starting_amount = 240

    # Calculate the number of games Joe can buy and sell
    num_games = (starting_amount - monthly_cost) // (monthly_cost - selling_price)

    # Calculate the number of months Joe can buy and sell games
    num_months = num_games + 1

    # Display the number of months
    result = num_months
    return result

print(solution())