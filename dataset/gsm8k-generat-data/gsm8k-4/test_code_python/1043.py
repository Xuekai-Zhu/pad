def solution():
    """James decides to buy a living room set. The coach cost $2500 and the sectional cost $3500 and everything else has a combined cost of $2000. He gets a 10% discount on everything. How much did he pay?"""
    # Define the prices of the couch, sectional, and other items
    couch_price = 2500
    sectional_price = 3500
    other_price = 2000

    # Calculate the total cost before discount
    total_cost = couch_price + sectional_price + other_price

    # Calculate the amount of discount
    discount = total_cost * 0.1

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    # Return the result
    result = total_cost_after_discount
    return result

print(solution())