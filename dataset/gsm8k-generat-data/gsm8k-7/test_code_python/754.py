def solution():
    price_alicia = 7.5
    price_brant = 10
    price_josh = 8.5
    price_yvette = 9

    # Calculate the total cost of all sundaes before tip
    subtotal = price_alicia + price_brant + price_josh + price_yvette

    # Calculate the amount of tip
    tip = subtotal * 0.2

    # Calculate the final bill amount
    total_cost = subtotal + tip
    result = total_cost
    return result

print(solution())