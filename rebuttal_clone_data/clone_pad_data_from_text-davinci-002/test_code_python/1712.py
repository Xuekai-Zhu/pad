def solution():
    shirts_bought = 6
    regular_price = 50
    discount_percent = 20
    discount_amount = shirts_bought * (discount_percent / 100) * regular_price
    total_price = shirts_bought * regular_price - discount_amount
    result = total_price
    
    return result

print(solution())