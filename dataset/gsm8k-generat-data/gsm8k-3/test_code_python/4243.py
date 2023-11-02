def solution():
    """A king gets a crown made that costs $20,000.  He tips the person 10%.  How much did the king pay after the tip?"""
    # Define the cost of the crown and tip percentage
    CROWN_COST = 20000
    TIP_PERCENTAGE = 0.1

    # Calculate the amount of the tip
    tip = CROWN_COST * TIP_PERCENTAGE

    # Calculate the total amount paid
    total_amount = CROWN_COST + tip

    # Display the total amount paid
    result = total_amount
    return result

print(solution())