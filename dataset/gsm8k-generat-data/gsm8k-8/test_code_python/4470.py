def solution():
    cabinet_price = 1200
    discount = 0.15

    # Calculate the amount of the discount
    discount_amount = cabinet_price * discount

    # Calculate the price after the discount
    price_after_discount = cabinet_price - discount_amount
    result = price_after_discount
    return result

print(solution())