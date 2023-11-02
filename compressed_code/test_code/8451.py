def solution():
    
    num_shirts = 3
    shirt_price = 20
    tax_rate = 0.1
    subtotal = num_shirts * shirt_price
    tax = tax_rate * subtotal
    total_cost = subtotal + tax
    result = total_cost
    return result

print(solution())