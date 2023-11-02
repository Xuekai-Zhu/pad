def solution():
    """Victoria had $500. She went to the market and bought 2 packets of rice each at $20, 3 packets of wheat flour each at $25, and 1 soda at $150. What was her remaining balance?"""
    # Define the cost of each item
    RICE_PRICE = 20
    FLOUR_PRICE = 25
    SODA_PRICE = 150

    # Define the quantity of each item purchased
    rice_quantity = 2
    flour_quantity = 3
    soda_quantity = 1

    # Calculate the total cost of the rice
    rice_cost = rice_quantity * RICE_PRICE

    # Calculate the total cost of the wheat flour
    flour_cost = flour_quantity * FLOUR_PRICE

    # Calculate the total cost of the soda
    soda_cost = soda_quantity * SODA_PRICE

    # Calculate the total cost of all the items
    total_cost = rice_cost + flour_cost + soda_cost

    # Calculate Victoria's remaining balance
    balance = 500 - total_cost

    # Display Victoria's remaining balance
    result = balance
    return result

print(solution())