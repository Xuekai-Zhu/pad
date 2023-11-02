def solution():
    initial_price = 600
    percent_discount = 20
    discount_amount = initial_price * (percent_discount / 100)
    sale_price = initial_price - discount_amount
    result = sale_price
    
    return result

print(solution())