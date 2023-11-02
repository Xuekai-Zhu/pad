def solution():
    """If eight movie tickets cost 2 times as much as one football game ticket, and each movie ticket is sold at $30, calculate the total amount of money Chandler will pay if he buys eight movie tickets and five football game tickets."""
    # Define the price of a movie ticket and the ratio of movie ticket price to football game ticket price
    MOVIE_PRICE = 30
    MOVIE_TO_FOOTBALL_RATIO = 2

    # Calculate the price of a football game ticket
    football_price = MOVIE_PRICE / MOVIE_TO_FOOTBALL_RATIO

    # Calculate the total cost of eight movie tickets
    movie_cost = 8 * MOVIE_PRICE

    # Calculate the total cost of five football game tickets
    football_cost = 5 * football_price

    # Calculate the total cost of all tickets
    total_cost = movie_cost + football_cost

    # Return the result
    result = total_cost
    return result

print(solution())