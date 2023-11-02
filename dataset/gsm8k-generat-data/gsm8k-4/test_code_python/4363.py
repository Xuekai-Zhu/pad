def solution():
    """Fabian is shopping at a nearby supermarket. He wants to buy 5 kilograms of apples, 3 packs of sugar, and 500 grams of walnuts. One kilogram of apples costs $2, and one kilogram of walnuts costs $6. One pack of sugar is $1 cheaper than one kilogram of apples. How much Fabian needs to pay for the items he wants to buy?"""
    # Define the quantity and price of apples
    apples_quantity = 5
    apples_price = 2

    # Calculate the total cost of apples
    apples_cost = apples_quantity * apples_price

    # Define the quantity and price of sugar
    sugar_quantity = 3
    sugar_price = apples_price - 1

    # Calculate the total cost of sugar
    sugar_cost = sugar_quantity * sugar_price

    # Define the quantity and price of walnuts
    walnuts_quantity = 0.5
    walnuts_price = 6

    # Calculate the total cost of walnuts
    walnuts_cost = walnuts_quantity * walnuts_price

    # Calculate the total cost of all items
    total_cost = apples_cost + sugar_cost + walnuts_cost
    
    result = total_cost
    return result

print(solution())