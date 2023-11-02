def solution():
    
    num_shirts = 3
    shirt_price = 20
    tax_rate = 0.1
    subtotal = num_shirts * shirt_price
    tax = subtotal * tax_rate
    total = subtotal + tax
    result = total
    return result

print(solution())