def solution():
    
    string_cost = 1
    bead_cost = 3
    sale_price = 6
    total_bracelets = 25
    total_cost = (string_cost + bead_cost) * total_bracelets
    total_revenue = sale_price * total_bracelets
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())