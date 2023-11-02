def solution():
    """James decides to buy a living room set.  The coach cost $2500 and the sectional cost $3500 and everything else has a combined cost of $2000.  He gets a 10% discount on everything.  How much did he pay?"""
    # Define the prices of the couch, sectional, and other items
    COUCH_PRICE = 2500
    SECTIONAL_PRICE = 3500
    OTHER_PRICE = 2000

    # Calculate the total cost of all the items
    total_cost = COUCH_PRICE + SECTIONAL_PRICE + OTHER_PRICE

    # Calculate the amount of the 10% discount
    discount = 0.1 * total_cost

    # Calculate the final cost after the discount
    final_cost = total_cost - discount

    # Display the final cost
    result = final_cost
    return result

print(solution())