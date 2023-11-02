def solution():
    """Big Lots is having a sale. All chairs are 25% off. If you buy more than 5 chairs, you get an additional 1/3 off the discounted price of the number of chairs over 5. If you bought 8 chairs that were normally priced at $20, how much do the chairs cost in total?"""
    num_chairs = 8
    chair_price = 20
    discounted_price = (1 - 0.25) * chair_price
    if num_chairs > 5:
        extra_discounted_price = (1 - (1/3)) * discounted_price * (num_chairs - 5)
        total_price = (discounted_price * 5) + extra_discounted_price
    else:
        total_price = discounted_price * num_chairs
    result = total_price
    return result

print(solution())