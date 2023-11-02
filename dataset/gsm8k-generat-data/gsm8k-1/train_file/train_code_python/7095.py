def solution():
    """Ken buys gummy vitamins. They are usually $15.00 per bottle at his grocery store, but they are currently 20% off. On top of that, he has 3 $2.00 coupons. How much will 3 bottles cost?"""
    original_price = 15.00
    percent_off = 20
    sale_price = original_price - (original_price * (percent_off / 100))
    num_bottles = 3
    total_cost = (sale_price * num_bottles) - (3 * 2.00)
    result = total_cost
    return result

print(solution())