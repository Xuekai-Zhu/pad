def solution():
    
    packages_3 = 3
    price_3 = 2.5
    packages_2 = 2
    price_2 = 1
    total_flowers = 18
    total_price = (packages_3 * price_3) + (packages_2 * price_2)
    savings = total_price - total_flowers
    result = savings
    return result

print(solution())