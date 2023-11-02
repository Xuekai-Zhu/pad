def solution():
    """Solomon bought a dining table at a 10% discount and paid the sale price of $450. What was the original price of the dining table?"""
    sale_price = 450
    discount_percent = 10
    original_price = sale_price / ((100-discount_percent) / 100)
    result = original_price
    return result

print(solution())