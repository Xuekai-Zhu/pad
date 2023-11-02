def solution():
    
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