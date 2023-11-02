def solution():
    
    shirt_price = 60
    jacket_price = 90
    discount = 0.2
    discount_shirt_price = shirt_price - (shirt_price * discount)
    discount_jacket_price = jacket_price - (jacket_price * discount)
    total_cost = (5 * discount_shirt_price) + (10 * discount_jacket_price)
    result = total_cost
    return result

print(solution())