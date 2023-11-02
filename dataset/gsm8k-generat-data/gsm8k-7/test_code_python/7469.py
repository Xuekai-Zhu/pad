def solution():
    num_bracelets = 12
    supply_cost_per_bracelet = 1
    selling_price_per_bracelet = 1.5
    remaining_money = 3

    # Calculate the total cost of supplies for all bracelets
    total_supply_cost = num_bracelets * supply_cost_per_bracelet

    # Calculate the total revenue from selling all bracelets
    total_revenue = num_bracelets * selling_price_per_bracelet

    # Calculate the total profit from selling all bracelets
    total_profit = total_revenue - total_supply_cost

    # Calculate the cost of the box of cookies
    box_of_cookies_cost = total_profit - remaining_money
    result = box_of_cookies_cost
    return result

print(solution())