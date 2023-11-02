def solution():
    """Zane purchases 2 polo shirts from the 40% off rack at the men’s store. The polo shirts are $50 each at the regular price. How much did he pay for the shirts?"""
    regular_price = 50
    discount_percent = 40
    discount_amount = regular_price * (discount_percent / 100)
    sale_price = regular_price - discount_amount
    number_of_shirts = 2
    total_price = sale_price * number_of_shirts
    result = total_price
    return result

print(solution())