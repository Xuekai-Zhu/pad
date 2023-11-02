def solution():
    num_bracelets = 52
    material_cost = 3.0
    num_bracelets_given_away = 8
    sale_price = 0.25

    # Calculate the total cost of materials for all bracelets
    total_material_cost = material_cost

    # Calculate the total number of bracelets sold
    num_bracelets_sold = num_bracelets - num_bracelets_given_away

    # Calculate the total revenue from selling the bracelets
    total_revenue = num_bracelets_sold * sale_price

    # Calculate the profit (revenue - cost)
    profit = total_revenue - total_material_cost
    result = profit
    return result

print(solution())