def solution():
    
    num_fandoms = 4
    num_shirts = 5
    shirt_price = 15
    sale_percent = 20
    tax_percent = 10
    subtotal = num_fandoms * num_shirts * shirt_price * (1 - sale_percent/100)
    tax_amount = subtotal * (tax_percent/100)
    total = subtotal + tax_amount
    result = total
    return result

print(solution())