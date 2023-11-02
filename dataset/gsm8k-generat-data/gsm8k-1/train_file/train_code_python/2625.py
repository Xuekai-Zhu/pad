def solution():
    """Mark wants to order a pair of slippers for his wife with her initials embroidered on top. The slippers are currently $50.00 and are 10% off. The embroidery will be $5.50 per shoe and shipping is a flat rate of $10.00. How much will the slippers cost?"""
    slippers_cost = 50.00 * 0.9
    embroidery_cost = 5.50 * 2
    shipping_cost = 10.00
    total_cost = slippers_cost + embroidery_cost + shipping_cost
    result = total_cost
    return result

print(solution())