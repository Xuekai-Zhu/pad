def solution():
    original_price = 125  # dollars
    sale_price = original_price * 0.8  # 20% off
    final_price = sale_price - 10  # coupon
    total_savings = original_price - final_price  # original price minus final price
    final_price_with_card = final_price * 0.9  # 10% off with store credit card
    total_savings_with_card = original_price - final_price_with_card  # original price minus final price with card
    result = total_savings_with_card
    return result

print(solution())