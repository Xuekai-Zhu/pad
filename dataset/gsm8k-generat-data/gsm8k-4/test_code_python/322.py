def solution():
    """A shady restaurant is charging customers gratuities after taxes without them being aware. If my total bill was $140, the sales tax in my city is 10%, I ordered a NY Striploin for $80, and I ordered a glass of wine for $10, how much did they charge me for gratuities?"""
    # Define the meal and drink prices
    meal_price = 80
    drink_price = 10

    # Calculate the subtotal
    subtotal = meal_price + drink_price

    # Calculate the tax and add it to the subtotal
    tax = subtotal * 0.1
    total = subtotal + tax

    # Calculate the gratuity
    gratuity = round((140 - total), 2)

    # Return the result
    return gratuity

print(solution())