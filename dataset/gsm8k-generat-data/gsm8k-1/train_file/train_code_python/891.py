def solution():
    """An auto shop has a part that Clark needs for $80. Clark buys 7 of them and got a discount. If Clark only had to pay $439, how much was the discount?"""
    part_cost = 80
    quantity = 7
    total_cost = part_cost * quantity
    discount = total_cost - 439
    result = discount
    return result

print(solution())