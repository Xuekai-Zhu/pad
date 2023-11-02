def solution():
    
    package_16oz_price = 7
    package_8oz_price = 4
    package_4oz_price = 2
    discount_percent = 50
    discount_amount = package_4oz_price * (discount_percent / 100)
    discounted_price = package_4oz_price - discount_amount
    total_discount_price = (discounted_price * 2) + package_8oz_price
    if total_discount_price < package_16oz_price:
        result = total_discount_price
    else:
        result = package_16oz_price
    return result

print(solution())