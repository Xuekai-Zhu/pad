def solution():
    """The treasurer of a football team must buy equipment for the sixteen players of his team. Each piece of equipment consists of a $25 jersey, a $15.20 pair of shorts and a pair of socks at $6.80. How much does all the equipment of all the players on the team cost?"""
    # Define the cost of each piece of equipment
    JERSEY_PRICE = 25
    SHORTS_PRICE = 15.20
    SOCKS_PRICE = 6.80

    # Define the number of players on the team
    NUM_PLAYERS = 16

    # Calculate the total cost of all the jerseys
    jersey_cost = JERSEY_PRICE * NUM_PLAYERS

    # Calculate the total cost of all the shorts
    shorts_cost = SHORTS_PRICE * NUM_PLAYERS

    # Calculate the total cost of all the socks
    socks_cost = SOCKS_PRICE * NUM_PLAYERS * 2

    # Calculate the total cost of all the equipment
    total_cost = jersey_cost + shorts_cost + socks_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())