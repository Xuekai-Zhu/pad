def solution():
    """Mrs. Petersons bought 10 tumblers for $45 each. She paid with five $100 bills. How much change will Mrs. Petersons receive?"""
    # Define the number of tumblers and the price per tumbler
    num_tumblers = 10
    tumbler_price = 45

    # Calculate the total cost of the tumblers
    total_cost = num_tumblers * tumbler_price

    # Define the amount paid
    amount_paid = 500

    # Calculate the change
    change = amount_paid - total_cost

    # return the result
    result = change
    return result

print(solution())