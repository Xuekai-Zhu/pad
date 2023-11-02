def solution():
    
    nike_price = 150
    boots_price = 120
    tax_rate = 0.1
    subtotal = nike_price + boots_price
    tax = subtotal * tax_rate
    total = subtotal + tax
    result = total
    return result

print(solution())