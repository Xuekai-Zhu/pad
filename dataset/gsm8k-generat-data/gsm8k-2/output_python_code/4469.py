def solution():
    """Tim buys a cabinet for $1200 and gets a 15% discount. How much did he pay?"""
    original_price = 1200
    discount_percentage = 15
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())