def solution():
    """Jackson buys a computer game for $66 and three movie tickets for $12 each. How much did he spend on entertainment total?"""
    # Define the cost of the computer game and movie tickets
    GAME_COST = 66
    TICKET_COST = 12

    # Calculate the cost of the movie tickets
    ticket_total = TICKET_COST * 3

    # Calculate the total cost of entertainment
    total_cost = GAME_COST + ticket_total

    # Display the total cost
    result = total_cost
    return result

print(solution())