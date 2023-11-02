def solution():
    
    subtotal = 40
    tax_rate = 0.05
    discount = 8

    
    total = (subtotal * (1 + tax_rate)) - discount

    
    cody_paid = total / 2

    result = cody_paid
    return result

print(solution())