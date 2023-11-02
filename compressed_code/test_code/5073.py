def solution():
    
    price_per_person = 147
    discount_per_person = 14
    total_discount = discount_per_person * 2
    total_price = price_per_person * 2 - total_discount
    result = total_price
    return result

print(solution())