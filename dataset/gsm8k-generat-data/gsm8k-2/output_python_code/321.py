def solution():
    """A shady restaurant is charging customers gratuities after taxes without them being aware. If my total bill was $140, the sales tax in my city is 10%, I ordered a NY Striploin for $80, and I ordered a glass of wine for $10, how much did they charge me for gratuities?"""
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