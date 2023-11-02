def solution():
    """Mark wants to order a pair of slippers for his wife with her initials embroidered on top.  The slippers are currently $50.00 and are 10% off.  The embroidery will be $5.50 per shoe and shipping is a flat rate of $10.00.  How much will the slippers cost?"""
    # Define the original price of the slippers
    original_price = 50.0

    # Calculate the sale price of the slippers
    sale_price = original_price * 0.9

    # Calculate the cost of embroidery for both shoes
    embroidery_cost = 5.5 * 2

    # Calculate the total cost of the slippers with embroidery and shipping
    total_cost = sale_price + embroidery_cost + 10.0

    # Display the total cost of the slippers
    result = total_cost
    return result

print(solution())