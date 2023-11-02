def solution():
    """Silvia’s bakery is offering 10% on advanced orders over $50.00. She orders 2 quiches for $15.00 each, 6 croissants at $3.00 each and 6 buttermilk biscuits for $2.00 each. How much will her order be with the discount?"""
    # Define the prices of items ordered
    quiche_price = 15.00
    croissant_price = 3.00
    biscuit_price = 2.00

    # Calculate the total cost of the order
    total_cost = 2 * quiche_price + 6 * croissant_price + 6 * biscuit_price

    # Check if the order is eligible for the discount
    if total_cost > 50.00:
        # Calculate the discount amount
        discount_amount = total_cost * 0.10
        # Apply the discount to the total cost
        total_cost -= discount_amount

    # Return the total cost of the order
    result = total_cost
    return result

print(solution())