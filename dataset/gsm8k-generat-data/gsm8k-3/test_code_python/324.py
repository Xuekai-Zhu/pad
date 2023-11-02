def solution():
    """A shady restaurant is charging customers gratuities after taxes without them being aware. If my total bill was $140, the sales tax in my city is 10%, I ordered a NY Striploin for $80, and I ordered a glass of wine for $10, how much did they charge me for gratuities?"""
    # Calculate the total cost of food and beverages
    food_cost = 80 + 10

    # Calculate the sales tax
    sales_tax = 0.1 * food_cost

    # Calculate the total bill
    total_bill = food_cost + sales_tax

    # Calculate the gratuities charged
    gratuities = 140 - total_bill

    # Display the gratuities charged
    result = gratuities
    return result

print(solution())