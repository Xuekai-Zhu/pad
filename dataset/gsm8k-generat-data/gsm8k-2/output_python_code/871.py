def solution():
    """John decided to buy 10 pins for himself. They are normally $20 each but they were on sale for 15% off. How much did he spend on pins?"""
    original_price = 20
    discount_percentage = 0.15
    sale_price = original_price - (original_price * discount_percentage)
    quantity = 10
    total_cost = sale_price * quantity
    result = total_cost
    return result

print(solution())