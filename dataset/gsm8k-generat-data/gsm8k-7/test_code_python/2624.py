def solution():
    discount = 40
    discount_percent = 0.25  # 25% discount

    # Calculate the original price of the DVDs
    original_price = discount / discount_percent

    # Calculate the price Maria paid after the discount
    price_paid = original_price - discount
    result = price_paid
    return result

print(solution())