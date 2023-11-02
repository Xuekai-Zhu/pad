def solution():
    
    regular_price = 50
    discount = 0.4
    num_shirts = 2
    discounted_price = regular_price * (1 - discount)
    total_price = discounted_price * num_shirts
    result = total_price
    return result

print(solution())