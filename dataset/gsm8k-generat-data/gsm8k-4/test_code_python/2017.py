def solution():
    """Jed’s family wants to buy 6 different board games. Each board game costs $15 and Jed paid using a $100 bill. If the cashier gave Jed only $5 bills for his change, how many bills did Jed receive?"""
    # Calculate the total cost of the board games
    total_cost = 6 * 15

    # Calculate the amount of change Jed received
    change = 100 - total_cost

    # Calculate the number of $5 bills in the change
    num_bills = change / 5

    # Round up to the nearest whole number
    num_bills = math.ceil(num_bills)

    # return the result
    result = num_bills
    return result

print(solution())