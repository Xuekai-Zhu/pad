def solution():
    
    regular_price = 50
    discount_percent = 40
    discount_amount = regular_price * (discount_percent / 100)
    sale_price = regular_price - discount_amount
    number_of_shirts = 2
    total_price = sale_price * number_of_shirts
    result = total_price
    return result

print(solution())