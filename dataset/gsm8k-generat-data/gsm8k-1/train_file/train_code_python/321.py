def solution():
    """A shady restaurant is charging customers gratuities after taxes without them being aware. If my total bill was $140, the sales tax in my city is 10%, I ordered a NY Striploin for $80, and I ordered a glass of wine for $10, how much did they charge me for gratuities?"""
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