def solution():
    # Calculate the amount Barry needs to pay after the discount
    original_price = 80
    discount_percentage = 15
    discount_amount = (discount_percentage / 100) * original_price
    amount_to_pay = original_price - discount_amount
    result = amount_to_pay
    return result

print(solution())