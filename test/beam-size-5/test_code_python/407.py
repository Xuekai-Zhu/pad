def solution():
    
    package_price = 400
    pack_price = package_price * 2
    discount = 0.2
    finale_price = 150
    discounted_price = (package_price - discount) * (1 - discount)
    total_price = discounted_price + finale_price
    result = total_price
    return result

print(solution())