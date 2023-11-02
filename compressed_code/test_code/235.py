def solution():
    
    total_bill = 140
    tax_rate = 0.1
    food_cost = 80
    wine_cost = 10
    subtotal = food_cost + wine_cost
    tax_amount = subtotal * tax_rate
    total_with_tax = subtotal + tax_amount
    gratuity_amount = total_bill - total_with_tax
    result = gratuity_amount
    return result

print(solution())