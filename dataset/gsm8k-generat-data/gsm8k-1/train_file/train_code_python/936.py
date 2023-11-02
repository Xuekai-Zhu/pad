def solution():
    """Stella wanted to buy a new dress for the upcoming dance. At the store she found out that the dress she wanted was $50. The store was offering 30% off of everything in the store. What was the final cost of the dress?"""
    original_cost = 50
    discount_percent = 30
    discount_amount = original_cost * (discount_percent / 100)
    final_cost = original_cost - discount_amount
    result = final_cost
    return result

print(solution())