def solution():
    """Axel bought an aquarium that was marked down 50% from an original price of $120. But he also paid additional sales tax equal to 5% of the reduced price. What was the total cost of the aquarium?"""
    original_price = 120
    discount = 0.5
    reduced_price = original_price * discount
    sales_tax_rate = 0.05
    tax_amount = reduced_price * sales_tax_rate
    total_cost = reduced_price + tax_amount
    result = total_cost
    return result

print(solution())