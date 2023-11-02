def solution():
    """Preston has a sandwich shop. He charges $5 for each sandwich. He also charges $20 for a delivery fee. Abra Company orders 18 sandwiches from Preston and also tips him 10%. How much total, in dollars, did Preston receive?"""
    # Define the price per sandwich and the delivery fee
    SANDWICH_PRICE = 5
    DELIVERY_FEE = 20

    # Calculate the total cost of the sandwiches
    sandwich_cost = 18 * SANDWICH_PRICE

    # Calculate the tip amount
    tip_amount = sandwich_cost * 0.1

    # Calculate the total amount received by Preston
    total_amount = sandwich_cost + DELIVERY_FEE + tip_amount

    # Return the result
    result = total_amount
    return result

print(solution())