def solution():
    cost_per_bracelet = 1
    revenue_per_bracelet = 1.5
    number_of_bracelets = 12
    total_spent = cost_per_bracelet * number_of_bracelets
    total_revenue = revenue_per_bracelet * number_of_bracelets
    net_revenue = total_revenue - total_spent
    cookies_cost = total_spent - net_revenue
    result = cookies_cost
    
    return result

print(solution())