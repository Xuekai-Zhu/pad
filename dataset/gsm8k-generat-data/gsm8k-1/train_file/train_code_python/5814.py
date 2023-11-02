def solution():
    """Eunice spent $7500 on a used car, which is 25% less than the original price. What was the original price of the car?"""
    price_after_discount = 7500
    percent_original_price = 100 / (100 - 25)
    original_price = percent_original_price * price_after_discount
    result = original_price
    return result

print(solution())