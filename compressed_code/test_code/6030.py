def solution():
    
    total_bill = 140
    tax_rate = 0.1
    food_total = 80
    drink_total = 10
    pre_tax_total = food_total + drink_total
    tax_amount = pre_tax_total * tax_rate
    subtotal = pre_tax_total + tax_amount
    gratuity = total_bill - subtotal
    result = gratuity
    
    return result

print(solution())