def solution():
    
    bottles_per_year = 12
    bottle_price = 30
    discount_percent = 30
    discount_amount = discount_percent / 100 * (bottles_per_year * bottle_price)
    total_price = (bottles_per_year * bottle_price) - discount_amount
    result = total_price
    return result

print(solution())