def solution():
    
    initial_price = 200
    tax_rate = 0.15
    tax_amount = initial_price * tax_rate
    total_price = initial_price + tax_amount
    result = total_price
    return result

print(solution())