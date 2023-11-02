def solution():
    """Mark wants to order a pair of slippers for his wife with her initials embroidered on top. The slippers are currently $50.00 and are 10% off. The embroidery will be $5.50 per shoe and shipping is a flat rate of $10.00. How much will the slippers cost?"""
    # Define the initial price of the slippers
    original_price = 50

    # Calculate the discounted price of the slippers
    discounted_price = original_price - (original_price * 0.1)

    # Calculate the total cost of the slippers with the embroidery and shipping
    total_cost = discounted_price + (5.5 * 2) + 10

    result = total_cost
    return result

print(solution())