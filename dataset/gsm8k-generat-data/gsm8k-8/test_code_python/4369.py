def solution():
    original_price = 10
    discount_percentage = 10
    discount_amount = (discount_percentage/100) * original_price
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())