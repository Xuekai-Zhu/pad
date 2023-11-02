def solution():
    
    num_sets = 5
    set_price = 6
    subtotal = num_sets * set_price
    tax_rate = 0.1
    tax = subtotal * tax_rate
    total_price = subtotal + tax
    result = total_price
    return result

print(solution())