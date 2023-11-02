def solution():
    """Leila went to the supermarket to buy food for the Christmas party. She bought apples for 5€, sugar for 3€ and carrots for 17€. She paid with a 50€ bill. How much money does the saleswoman return to her?"""
    # Define the prices of the items and the amount paid
    apples_price = 5
    sugar_price = 3
    carrots_price = 17
    amount_paid = 50

    # Calculate the total cost of the items
    total_cost = apples_price + sugar_price + carrots_price

    # Calculate the amount of change
    change = amount_paid - total_cost

    # Return the result
    result = change
    return result

print(solution())