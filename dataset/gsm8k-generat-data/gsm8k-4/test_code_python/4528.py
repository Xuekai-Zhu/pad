def solution():
    """The treasurer of a football team must buy equipment for the sixteen players of his team. Each piece of equipment consists of a $25 jersey, a $15.20 pair of shorts and a pair of socks at $6.80. How much does all the equipment of all the players on the team cost?"""
    # Define the prices of the equipment pieces
    JERSEY_PRICE = 25
    SHORTS_PRICE = 15.20
    SOCKS_PRICE = 6.80

    # Define the number of players
    NUM_PLAYERS = 16

    # Calculate the total cost of the equipment for all players
    total_cost = (JERSEY_PRICE + SHORTS_PRICE + SOCKS_PRICE) * NUM_PLAYERS

    # Return the result
    result = round(total_cost, 2)
    return result

print(solution())