def solution():
    original_price = 50
    discount_percentage = 30
    discount_amount = original_price * (discount_percentage/100)
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())