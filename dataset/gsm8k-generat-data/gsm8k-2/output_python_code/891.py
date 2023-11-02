def solution():
    """An auto shop has a part that Clark needs for $80. Clark buys 7 of them and got a discount. If Clark only had to pay $439, how much was the discount?"""
    part_price = 80
    total_price = part_price * 7
    discount = total_price - 439
    result = discount
    return result

print(solution())