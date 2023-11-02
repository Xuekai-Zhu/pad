def solution():
    """Zane purchases 2 polo shirts from the 40% off rack at the men’s store. The polo shirts are $50 each at the regular price. How much did he pay for the shirts?"""
    regular_price = 50
    discount = 0.4
    num_shirts = 2
    discounted_price = regular_price * (1 - discount)
    total_price = discounted_price * num_shirts
    result = total_price
    return result

print(solution())