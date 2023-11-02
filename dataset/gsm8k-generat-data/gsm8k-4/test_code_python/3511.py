def solution():
    """Victoria had $500. She went to the market and bought 2 packets of rice each at $20, 3 packets of wheat flour each at $25, and 1 soda at $150. What was her remaining balance?"""
    # Define the initial amount of money Victoria had
    initial_amount = 500

    # Define the prices of rice, wheat flour, and soda
    rice_price = 20
    flour_price = 25
    soda_price = 150

    # Calculate the total cost of rice
    rice_cost = 2 * rice_price

    # Calculate the total cost of wheat flour
    flour_cost = 3 * flour_price

    # Calculate the total cost of soda
    soda_cost = soda_price

    # Calculate the total cost of the items
    total_cost = rice_cost + flour_cost + soda_cost

    # Calculate the remaining balance
    remaining_balance = initial_amount - total_cost

    # Display the remaining balance
    result = remaining_balance
    return result

print(solution())