def solution():
    """Solomon bought a dining table at a 10% discount and paid the sale price of $450. What was the original price of the dining table?"""
    sale_price = 450
    discount = 0.1
    original_price = sale_price / (1 - discount)
    result = original_price
    return result

print(solution())