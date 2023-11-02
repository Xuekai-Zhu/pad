def solution():
    """Adam bought 3 kilograms of nuts and 2.5 kilograms of dried fruits at a store. One kilogram of nuts costs $12 and one kilogram of dried fruit costs $8. How much did his purchases cost?"""
    # Define the prices and quantities of nuts and dried fruits
    nut_price = 12
    nut_quantity = 3
    fruit_price = 8
    fruit_quantity = 2.5

    # Calculate the total cost of nuts and dried fruits
    total_nut_cost = nut_price * nut_quantity
    total_fruit_cost = fruit_price * fruit_quantity
    total_cost = total_nut_cost + total_fruit_cost

    # Return the result
    result = total_cost
    return result

print(solution())