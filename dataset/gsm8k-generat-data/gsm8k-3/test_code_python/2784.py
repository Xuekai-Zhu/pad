def solution():
    """Rubble has $15 in his pocket and he needs to buy 2 notebooks and 2 pens. Each notebook cost $4.00 meanwhile each pen cost $1.50. How much money will be left from Rubble after the purchase?"""
    # Define the cost of each item
    NOTEBOOK_COST = 4.00
    PEN_COST = 1.50

    # Define the number of each item to be purchased
    notebooks = 2
    pens = 2

    # Calculate the total cost of the items
    total_cost = notebooks * NOTEBOOK_COST + pens * PEN_COST

    # Calculate the money left after the purchase
    money_left = 15 - total_cost

    # Display the money left
    result = money_left
    return result

print(solution())