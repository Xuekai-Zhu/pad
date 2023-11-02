def solution():
    """Silvia’s bakery is offering 10% on advanced orders over $50.00.  She orders 2 quiches for $15.00 each, 6 croissants at $3.00 each and 6 buttermilk biscuits for $2.00 each.  How much will her order be with the discount?"""
    # Define the prices of the items
    quiche_price = 15
    croissant_price = 3
    biscuit_price = 2

    # Calculate the total cost of the order
    total_cost = (2 * quiche_price) + (6 * croissant_price) + (6 * biscuit_price)

    # Apply the discount if the order is over $50
    if total_cost > 50:
        discount = total_cost * 0.1
        total_cost -= discount

    # Round the total cost to 2 decimal places
    result = round(total_cost, 2)
    return result

print(solution())