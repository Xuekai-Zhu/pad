def solution():
    
    sugar_price = 1.5
    salt_price = (5.5 - 2*sugar_price) / 5
    total_price = 3*sugar_price + salt_price
    result = total_price
    return result

print(solution())