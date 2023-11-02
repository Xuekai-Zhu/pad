def solution():
    
    num_washes = 20
    regular_price = 15
    discount = 0.6
    price_per_wash = regular_price * discount
    package_price = num_washes * price_per_wash
    result = package_price
    return result

print(solution())