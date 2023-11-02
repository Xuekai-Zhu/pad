def solution():
    """Mrs. Petersons bought 10 tumblers for $45 each. She paid with five $100 bills. How much change will Mrs. Petersons receive?"""
    # Define the cost of each tumbler
    TUMBLER_COST = 45

    # Define the number of tumblers purchased
    num_tumblers = 10

    # Calculate the total cost of the tumblers
    total_cost = num_tumblers * TUMBLER_COST

    # Calculate the amount Mrs. Petersons paid
    amount_paid = 5 * 100

    # Calculate the change Mrs. Petersons will receive
    change = amount_paid - total_cost

    # Display the change
    result = change
    return result

print(solution())