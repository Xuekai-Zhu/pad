def solution():
    """Axel bought an aquarium that was marked down 50% from an original price of $120. But he also paid additional sales tax equal to 5% of the reduced price. What was the total cost of the aquarium?"""
    original_price = 120
    discount_price = 0.5 * original_price
    sales_tax = 0.05 * discount_price
    total_cost = discount_price + sales_tax
    result = total_cost
    return result

print(solution())