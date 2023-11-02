def solution():
    
    tv_price = 1700
    tax_percent = 15
    tax_amount = tv_price * (tax_percent / 100)
    total_price = tv_price + tax_amount
    result = total_price
    return result

print(solution())