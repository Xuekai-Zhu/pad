def solution():
    """Stella wanted to buy a new dress for the upcoming dance. At the store she found out that the dress she wanted was $50. The store was offering 30% off of everything in the store. What was the final cost of the dress?"""
    original_price = 50
    discount_percent = 30
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())