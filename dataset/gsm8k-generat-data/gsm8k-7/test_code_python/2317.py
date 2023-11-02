def solution():
    lobster_price = 25.5
    steak_price = 35.0
    cheeseburger_price = 13.5
    appetizer_price = 8.5
    dessert_price = 6.0
    num_people = 4
    tip_percent = 0.2  # 20% tip

    # Calculate the total cost of the entrees
    entree_cost = lobster_price + steak_price + (2 * cheeseburger_price)

    # Calculate the total cost of the appetizer and desserts
    extras_cost = appetizer_price + (num_people * dessert_price)

    # Calculate the subtotal before tip
    subtotal = entree_cost + extras_cost

    # Calculate the tip
    tip = subtotal * tip_percent

    # Calculate the total cost with tip
    total_cost = subtotal + tip
    result = total_cost
    return result

print(solution())