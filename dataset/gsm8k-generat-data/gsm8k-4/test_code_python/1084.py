def solution():
    """If Billy and Jenny each order a $20 steak along with a $5 drink, how much will Billy have to pay in tips if he wants to cover 80% of a 20% tip for the two of them?"""
    # Define the cost of the meals and the cost of the drinks
    meal_cost = 20
    drink_cost = 5

    # Calculate the total cost of the meals and drinks, and the 20% tip amount
    total_cost = (meal_cost * 2) + (drink_cost * 2)
    tip_amount = total_cost * 0.2

    # Calculate the amount Billy needs to pay for 80% of the tip
    billy_tip = tip_amount * 0.8

    # Return the result
    result = billy_tip
    return result

print(solution())