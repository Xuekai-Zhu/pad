def solution():
    """If Billy and Jenny each order a $20 steak along with a $5 drink, how much will Billy have to pay in tips if he wants to cover 80% of a 20% tip for the two of them?"""
    # Define the cost of each steak and drink
    STEAK_COST = 20
    DRINK_COST = 5

    # Calculate the total cost of the meal for both Billy and Jenny
    meal_cost = (STEAK_COST + DRINK_COST) * 2

    # Calculate the 20% tip for the meal
    tip_amount = meal_cost * 0.2

    # Calculate the amount Billy needs to pay for 80% of the tip
    billy_tip = tip_amount * 0.8

    # Display the amount Billy needs to pay for the tip
    result = billy_tip
    return result

print(solution())