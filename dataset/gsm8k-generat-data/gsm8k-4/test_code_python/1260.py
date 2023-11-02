def solution():
    """Jackson buys a computer game for $66 and three movie tickets for $12 each. How much did he spend on entertainment total?"""
    # Define the prices of the computer game and movie tickets
    game_price = 66
    ticket_price = 12

    # Calculate the total cost of the movie tickets
    total_tickets_cost = 3 * ticket_price

    # Calculate the total spent on entertainment
    total_entertainment_cost = game_price + total_tickets_cost

    # return the result
    result = total_entertainment_cost
    return result

print(solution())