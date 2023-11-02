def solution():
    """Two sisters go to the movies. Movie tickets are $8 per person. If the sisters brought $25 with them, how much change will they receive after buying the tickets?"""
    # Define the cost of one movie ticket and the amount of money the sisters brought
    TICKET_COST = 8
    MONEY_BROUGHT = 25

    # Calculate the total cost of two movie tickets
    total_cost = TICKET_COST * 2

    # Calculate the amount of change the sisters will receive
    change = MONEY_BROUGHT - total_cost

    # Return the amount of change
    result = change
    return result

print(solution())