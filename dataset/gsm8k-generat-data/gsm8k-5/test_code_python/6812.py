def solution():
    bracelets_made = 52 # Alice made 52 friendship bracelets over spring break
    cost_of_materials = 3.00 # It cost Alice $3.00 in materials to make the bracelets
    bracelets_given_away = 8 # Alice gave 8 bracelets away during the break
    bracelets_sold = bracelets_made - bracelets_given_away # Alice sold all the remaining bracelets
    price_per_bracelet = 0.25 # Alice sold each bracelet at $0.25

    # Calculate the total revenue from selling the bracelets
    total_revenue = bracelets_sold * price_per_bracelet

    # Calculate the profit made by Alice
    profit = total_revenue - cost_of_materials
    result = profit
    return result

print(solution())