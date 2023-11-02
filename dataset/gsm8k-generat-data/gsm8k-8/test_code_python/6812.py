def solution():
    # Calculate the total cost of materials
    material_cost = 3

    # Calculate the total number of bracelets made
    total_bracelets = 52

    # Calculate the number of bracelets given away
    given_away = 8

    # Calculate the number of bracelets sold
    sold = total_bracelets - given_away

    # Calculate the revenue from selling the bracelets
    revenue = sold * 0.25

    # Calculate the profit
    profit = revenue - material_cost

    result = profit
    return result

print(solution())