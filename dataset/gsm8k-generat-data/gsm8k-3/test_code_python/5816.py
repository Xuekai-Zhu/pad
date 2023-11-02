def solution():
    """If eight movie tickets cost 2 times as much as one football game ticket, and each movie ticket is sold at $30, calculate the total amount of money Chandler will pay if he buys eight movie tickets and five football game tickets."""
    # Define the price of one movie ticket and the price ratio between a movie ticket and a football game ticket
    MOVIE_PRICE = 30
    PRICE_RATIO = 2
    # Calculate the price of one football game ticket
    FOOTBALL_PRICE = MOVIE_PRICE / PRICE_RATIO
    # Calculate the total cost of eight movie tickets
    movie_cost = 8 * MOVIE_PRICE
    # Calculate the total cost of five football game tickets
    football_cost = 5 * FOOTBALL_PRICE
    # Calculate the total amount Chandler will pay
    total_cost = movie_cost + football_cost
    # Display the total amount
    result = total_cost
    return result

print(solution())