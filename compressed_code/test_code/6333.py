def solution():
    
    string_cost = 1
    bead_cost = 3
    sale_price = 6
    bracelets_sold = 25
    total_cost = (string_cost + bead_cost) * bracelets_sold
    total_sales = sale_price * bracelets_sold
    profit = total_sales - total_cost
    result = profit
    return result

print(solution())