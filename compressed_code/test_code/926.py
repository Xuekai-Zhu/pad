def solution():
    
    nikes_price = 150
    work_boots_price = 120
    subtotal = nikes_price + work_boots_price
    tax_rate = 0.1
    total_price = subtotal * (1 + tax_rate)
    result = total_price
    return result

print(solution())