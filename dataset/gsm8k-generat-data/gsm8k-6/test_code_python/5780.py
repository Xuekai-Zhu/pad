def solution():
    # Calculate the price Travis needs to pay for his ticket with the student discount
    regular_price = 2000
    discount = 0.3
    discount_amount = regular_price * discount
    price_with_discount = regular_price - discount_amount
    result = price_with_discount
    return result

print(solution())