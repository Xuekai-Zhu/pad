def solution():
    # Calculate the cost of the main meals
    meal_cost = 12.0 * 4

    # Calculate the cost of the appetizers
    appetizer_cost = 6.0 * 2

    # Calculate the subtotal before tip and rush order fee
    subtotal = meal_cost + appetizer_cost

    # Calculate the 20% tip
    tip = 0.2 * subtotal

    # Add the rush order fee
    rush_order_fee = 5.0

    # Calculate the total cost
    total_cost = subtotal + tip + rush_order_fee

    result = total_cost
    return result

print(solution())