def solution():
    """Mac loves the shape of quarters and is willing to trade money for them, even if he loses value. He tells his brother that he will trade him 3 dimes for a quarter or 7 nickels. He trades for 20 quarters with dimes and 20 quarters with nickels. How many dollars did Mac lose?"""
    # Define the value of a dime and a nickel in cents
    DIME_VALUE = 10
    NICKEL_VALUE = 5

    # Define the number of dimes and nickels needed to trade for a quarter
    DIMES_PER_QUARTER = 3
    NICKELS_PER_QUARTER = 7

    # Define the number of quarters traded with dimes and nickels
    QUARTERS_WITH_DIMES = 20
    QUARTERS_WITH_NICKELS = 20

    # Calculate the number of dimes and nickels needed for the trades
    dimes_needed = QUARTERS_WITH_DIMES * DIMES_PER_QUARTER
    nickels_needed = QUARTERS_WITH_NICKELS * NICKELS_PER_QUARTER

    # Calculate the total value of the dimes and nickels
    total_value = (dimes_needed * DIME_VALUE) + (nickels_needed * NICKEL_VALUE)

    # Calculate the total value of the quarters received
    quarters_received = QUARTERS_WITH_DIMES + QUARTERS_WITH_NICKELS
    total_quarter_value = quarters_received * 25

    # Calculate the loss in value for Mac
    loss = total_value - total_quarter_value

    # Convert the loss to dollars
    loss_in_dollars = loss / 100

    # Return the loss in dollars
    result = loss_in_dollars
    return result

print(solution())